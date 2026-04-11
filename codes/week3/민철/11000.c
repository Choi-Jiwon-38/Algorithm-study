#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 저번에 만들어놓은 힙 구조 그대로 사용
typedef struct { long long val; int id; } Node;

typedef struct { int s, e; } Lecture;

void push(Node x, Node* h, int* s) {
    h[++(*s)] = x;
    for (int i = *s; i > 1 && h[i].val < h[i / 2].val; i /= 2) {
        Node t = h[i]; h[i] = h[i / 2]; h[i / 2] = t;
    }
}

Node pop(Node* h, int* s) {
    Node res = h[1]; h[1] = h[(*s)--];
    for (int i = 1; i * 2 <= *s; ) {
        int c = i * 2;
        if (c + 1 <= *s && h[c + 1].val < h[c].val) c++;
        if (h[c].val < h[i].val) { Node t = h[i]; h[i] = h[c]; h[c] = t; i = c; }
        else break;
    }
    return res;
}

// qsort 비교용 시작 시간 기준, 같으면 종료 시간 기준
int cmp(const void *a, const void *b) {
    Lecture *l1 = (Lecture *)a, *l2 = (Lecture *)b;
    if (l1->s != l2->s) return l1->s - l2->s;
    return l1->e - l2->e;
}

Lecture L[200005];
Node heap[200005];
int sz = 0;

int main() {
    char buf[64];
    if (!fgets(buf, 64, stdin)) return 0;
    int n = atoi(buf);

    for (int i = 0; i < n; i++) {
        if (fgets(buf, 64, stdin)) {
            sscanf(buf, "%d %d", &L[i].s, &L[i].e);
        }
    }

    // A의 Ti, B의 Si가 Ti <= Si 라면 같은 강의실이 가능하단걸 이용해야함
    // 위처럼 된다면 A의 Ti를 B의 Ti로 변경 후에 B를 삭제할 수 있음
    // 시작시간 기준 정렬 - 그리디니깐 뒷일은 모르겠고 앞부터 시작하자잉
    qsort(L, n, sizeof(Lecture), cmp);

    // 첫 강의 종료 시간
    push((Node){L[0].e, 0}, heap, &sz);

    for (int i = 1; i < n; i++) {
        // 가장 빨리 끝나는 방의 종료 시간 <= 현재 강의 시작 시간 이라면
        if (heap[1].val <= L[i].s) {
            pop(heap, &sz); // 기존 강의실 재사용을 위해 이전 종료 시간 제거
        }
        // 현재 강의의 종료 시간 추가
        push((Node){L[i].e, 0}, heap, &sz);
    }

    // 힙에 남은 데이터 개수가 필요한 총 강의실 수
    printf("%d\n", sz);

    return 0;
}
