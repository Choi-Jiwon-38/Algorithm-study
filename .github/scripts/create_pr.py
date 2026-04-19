"""
주차별 PR 자동 생성 스크립트
- codes/ 폴더의 기존 week 디렉토리를 보고 다음 주차 번호 자동 결정
- week{N} 브랜치 1개 생성
- codes/week{N}/README.md 1개 커밋 (기존 README 형식 동일)
- main으로 향하는 PR 1개 오픈
- Reviewer: Choi-Jiwon-38, AIJeongwon, jinh-636
"""

import os
import json
import base64
import re
import requests

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO = os.environ.get("GITHUB_REPOSITORY", "Choi-Jiwon-38/Algorithm-study")
HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

REVIEWERS = ["Choi-Jiwon-38", "AIJeongwon", "jinh-636"]


def make_url(slug):
    return f"https://leetcode.com/problems/{slug}/"


# ── GitHub API 헬퍼 ──────────────────────────────────────────────────────────

def get_week_numbers_from_branches():
    """열려있는 브랜치에서 week* 번호 목록 반환"""
    weeks = []
    page = 1
    while True:
        resp = requests.get(
            f"https://api.github.com/repos/{REPO}/branches?per_page=100&page={page}",
            headers=HEADERS,
        )
        if resp.status_code != 200 or not resp.json():
            break
        for b in resp.json():
            m = re.match(r"week(\d+)$", b["name"])
            if m:
                weeks.append(int(m.group(1)))
        if "next" not in resp.links:
            break
        page += 1
    return weeks


def get_week_numbers_from_main():
    """main 브랜치의 codes/ 디렉토리에서 week* 번호 목록 반환"""
    weeks = []
    resp = requests.get(
        f"https://api.github.com/repos/{REPO}/contents/codes",
        headers=HEADERS,
    )
    if resp.status_code != 200:
        return weeks
    for item in resp.json():
        if item["type"] == "dir":
            m = re.match(r"week(\d+)$", item["name"])
            if m:
                weeks.append(int(m.group(1)))
    return weeks


def get_next_week_number():
    """
    1순위: 열려있는 브랜치의 week* 중 최댓값 + 1
    2순위: 브랜치가 없으면 main의 codes/week* 디렉토리 최댓값 + 1
    """
    weeks = get_week_numbers_from_branches()
    if not weeks:
        print("ℹ️  열린 week 브랜치 없음 → main 디렉토리에서 주차 감지")
        weeks = get_week_numbers_from_main()
    return max(weeks) + 1 if weeks else 14


def get_main_sha():
    resp = requests.get(
        f"https://api.github.com/repos/{REPO}/git/ref/heads/main",
        headers=HEADERS,
    )
    resp.raise_for_status()
    return resp.json()["object"]["sha"]


def branch_exists(branch):
    return requests.get(
        f"https://api.github.com/repos/{REPO}/git/ref/heads/{branch}",
        headers=HEADERS,
    ).status_code == 200


def create_branch(branch, sha):
    requests.post(
        f"https://api.github.com/repos/{REPO}/git/refs",
        headers=HEADERS,
        json={"ref": f"refs/heads/{branch}", "sha": sha},
    ).raise_for_status()


def get_file_sha(path, branch):
    resp = requests.get(
        f"https://api.github.com/repos/{REPO}/contents/{path}?ref={branch}",
        headers=HEADERS,
    )
    return resp.json().get("sha") if resp.status_code == 200 else None


def commit_file(path, content, message, branch):
    payload = {
        "message": message,
        "content": base64.b64encode(content.encode()).decode(),
        "branch": branch,
    }
    existing_sha = get_file_sha(path, branch)
    if existing_sha:
        payload["sha"] = existing_sha
    requests.put(
        f"https://api.github.com/repos/{REPO}/contents/{path}",
        headers=HEADERS,
        json=payload,
    ).raise_for_status()


def pr_exists(head):
    resp = requests.get(
        f"https://api.github.com/repos/{REPO}/pulls?state=open&head={REPO.split('/')[0]}:{head}",
        headers=HEADERS,
    )
    return resp.status_code == 200 and len(resp.json()) > 0


def build_readme(week, problems):
    """기존 README 형식과 동일하게 생성
    예:
    # 14주차 알고리즘 문항

    * [Two Sum](https://leetcode.com/problems/two-sum/)
    * [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
    * [House Robber](https://leetcode.com/problems/house-robber/)
    * [Course Schedule](https://leetcode.com/problems/course-schedule/)
    """
    lines = [f"# {week}주차 알고리즘 문항\n"]
    for p in problems:
        lines.append(f"* [{p['title']}]({make_url(p['slug'])})")
    return "\n".join(lines) + "\n"


def create_pr(week, branch, problems, issue_number):
    problem_list = "\n".join(
        f"- [{p['title']}]({make_url(p['slug'])})" for p in problems
    )
    body = f"""## {week}주차 풀이

### 📋 이번 주 문제
{problem_list}

### 💬 리뷰 요청 사항
<!-- 리뷰어에게 특별히 확인받고 싶은 부분이 있으면 작성해주세요 -->

Closes #{issue_number}

---
*이 PR은 GitHub Actions에 의해 자동 생성되었습니다.*
"""
    resp = requests.post(
        f"https://api.github.com/repos/{REPO}/pulls",
        headers=HEADERS,
        json={
            "title": f"[Week {week:02d}] 풀이",
            "body": body,
            "head": branch,
            "base": "main",
        },
    )
    resp.raise_for_status()
    pr = resp.json()

    requests.post(
        f"https://api.github.com/repos/{REPO}/pulls/{pr['number']}/requested_reviewers",
        headers=HEADERS,
        json={"reviewers": REVIEWERS},
    )
    return pr


# ── 메인 ────────────────────────────────────────────────────────────────────

def main():
    print("📂 problems.json 읽는 중...")
    with open("problems.json", encoding="utf-8") as f:
        data = json.load(f)

    problems: list = data["problems"]
    issue_number: int = data["issue_number"]

    # problems.json의 week 대신 실제 레포 폴더 기준으로 주차 결정
    week = get_next_week_number()
    branch = f"week{week}"

    print(f"📅 {week}주차 / 문제 {len(problems)}개 / Issue #{issue_number}")
    print(f"🌿 브랜치: {branch}")

    main_sha = get_main_sha()

    # ── 1. 브랜치 생성 ─────────────────────────────────────────────────────────
    if branch_exists(branch):
        print("⚠️  브랜치 이미 존재, 스킵")
    else:
        create_branch(branch, main_sha)
        print("✅ 브랜치 생성 완료")

    # ── 2. README.md 1개 커밋 ──────────────────────────────────────────────────
    readme_path = f"codes/week{week}/README.md"
    readme_content = build_readme(week, problems)
    commit_file(
        path=readme_path,
        content=readme_content,
        message=f"chore: [Week {week}] README 추가",
        branch=branch,
    )
    print(f"📄 {readme_path} 커밋 완료")

    # ── 3. PR 생성 ─────────────────────────────────────────────────────────────
    if pr_exists(branch):
        print("⚠️  PR 이미 존재, 스킵")
    else:
        pr = create_pr(week, branch, problems, issue_number)
        print(f"🚀 PR 생성 완료: {pr['html_url']}")

    print("\n🎉 전체 완료!")


if __name__ == "__main__":
    main()
