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

Node mxH[1000001], mnH[1000001];
int mxS, mnS, vld[1000001]; // 최대 최소 힙이랑 D 연산 처리용 배열

int main() {
    char buf[64]; fgets(buf, 64, stdin); int T = atoi(buf); // 테스트 개수
    while (T--) { //T번 반복
        fgets(buf, 64, stdin); int k = atoi(buf), id = 0;
        mxS = mnS = 0; // k, 힙 등등 초기화
        for (int i = 0; i < k; i++) { // k번 반복
            char c; int n; fgets(buf, 64, stdin); sscanf(buf, " %c %d", &c, &n);
            if (c == 'I') { // I 명령 -> 삽입
                push((Node){n, id}, mnH, &mnS);
                push((Node){-n, id}, mxH, &mxS);
                vld[id++] = 1;
            } else { // 그 외는 D만 존재하니깐 삭제 명령
                if (n == 1) { // 최대 삭제
                    while (mxS && !vld[mxH[1].id]) pop(mxH, &mxS); // vld 배열에서 삭제처리(0 값이면 삭제) 했는지
                    if (mxS) vld[pop(mxH, &mxS).id] = 0;
                } else { // 최소 삭제
                    while (mnS && !vld[mnH[1].id]) pop(mnH, &mnS); // 확인 후 최대/최소 값 삭제
                    if (mnS) vld[pop(mnH, &mnS).id] = 0;
                }
            }
        }
        while (mxS && !vld[mxH[1].id]) pop(mxH, &mxS); // D 연산에서 했던거 마지막으로 한번 더
        while (mnS && !vld[mnH[1].id]) pop(mnH, &mnS); // D 연산으로 끝난 경우를 대비
        if (!mxS) printf("EMPTY\n"); // mxS 든 mnS든 상관 없음 그냥 있나없나 확인
        else printf("%lld %lld\n", -mxH[1].val, mnH[1].val);
    }
    return 0;
}
