#include <bits/stdc++.h>

using namespace std;

struct dir {
    int par_dir_idx;
    unordered_map<string, int> files;
};

int d_idx = 1; // 0: Main
unordered_map<string, int> idx_map;
unordered_multimap<string, string> d_relation, f_relation;
dir dir_map[1001];

string get_dirname(const string& path) {
    int slash_idx = path.find_last_of('/');
    
    if (slash_idx == string().npos)
        return path;
    else
        return path.substr(slash_idx + 1);
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, M;
    cin >> N >> M;
    
    // main 폴더 생성
    idx_map.insert({"main", 0});
    dir_map[0].par_dir_idx = -1;

    // 폴더 생성
    for (int i=0; i<N+M; i++) {
        string par, sub;
        int type;
        cin >> par >> sub >> type;
        if (type == 1) {
            // 자식 폴더 생성
            idx_map.insert({sub, d_idx});
            d_idx++;

            // 부모 - 자식 관계 저장
            d_relation.insert({par, sub});
        }
        else {
            // 폴더 - 파일 관계 저장
            f_relation.insert({par, sub});
        }
    }

    // 부모 - 자식 폴더 연결
    for (auto [par, sub]: d_relation) {
        int par_idx = idx_map[par], sub_idx = idx_map[sub];
        dir& sub_dir = dir_map[sub_idx];
        sub_dir.par_dir_idx = par_idx;
    }

    // 파일 생성
    for (auto [dir_name, f_name]: f_relation) {
        int cur_idx = idx_map[dir_name];
        while (cur_idx != -1) {
            dir &cur_dir = dir_map[cur_idx];
            auto& cur_files = cur_dir.files;
            
            // 파일이 있는 경우
            if (cur_files.find(f_name) != cur_files.end())
                cur_files[f_name]++;
            // 파일이 없는 경우
            else
                cur_files.insert({f_name, 1});

            // 부모 폴더에도 기록
            cur_idx = cur_dir.par_dir_idx;
        }
    }

    // 쿼리 처리
    int q;
    cin >> q;
    while (q--) {
        int cnt = 0;
        string path, dirname;

        cin >> path;
        dirname = get_dirname(path);

        int cur_idx = idx_map[dirname];
        dir& cur_dir = dir_map[cur_idx];
        for (auto [f_name, f_cnt]: cur_dir.files)
            cnt += f_cnt;
        cout << cur_dir.files.size() << ' ' << cnt << '\n';
    }
}