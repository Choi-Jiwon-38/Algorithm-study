#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { long long val; int id; } Node;

// x: 데이터, h: 힙 배열, s: 크기 포인터
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

Node heap[100001]; // 연산 개수
int sz = 0;

int main() {
    char buf[64];
    fgets(buf, 64, stdin); // 첫 줄은 연산 개수
    int n = atoi(buf);
    while (n--) {
        fgets(buf, 64, stdin); // 연산 읽기
        int x = atoi(buf);
        if (x == 0) { // 0이면 최대 출력 후 제거
            if (sz == 0) printf("0\n"); // 비어 있으면 0 출력
            else printf("%lld\n", -pop(heap, &sz).val); // 아래 push도 같지만 최소 힙으로 통일 시켜놔서 부호 반대
        } else { // 자연수면 추가
            push((Node){-x, 0}, heap, &sz);
        }
    }
    return 0;
}
