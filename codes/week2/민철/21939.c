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

Node maxH[200005], minH[200005]; // 최대 힙/ 최소 힙
int maxS = 0, minS = 0, curL[100001]; // 난이도 배열

int main() {
    char buf[64], cmd[15];
    int n, m, p, l, x;

    fgets(buf, 64, stdin); // 문제 개수
    n = atoi(buf);

    while (n--) { // 처음 문제 개수 들어오면 문제만 들어와서 따로 구분 X
        fgets(buf, 64, stdin); sscanf(buf, "%d %d", &p, &l);
        curL[p] = l; // 난이도 
        push((Node){(long long)l * 1000000 + p, p}, minH, &minS); // 문제 번호가 최대 10만이라 난이도 / 문제번호 순으로
        push((Node){(long long)-l * 1000000 - p, p}, maxH, &maxS); // 같은 난이도일 때 문제번호로 구분해야함
    }
    fgets(buf, 64, stdin); m = atoi(buf); // 명령 개수
    while (m--) { 
        fgets(buf, 64, stdin); sscanf(buf, "%s %d %d", cmd, &p, &l);
        if (cmd[0] == 'a') { // 문제 추가, 위와 동일
            curL[p] = l;
            push((Node){(long long)l * 1000000 + p, p}, minH, &minS);
            push((Node){(long long)-l * 1000000 - p, p}, maxH, &maxS);
        } else if (cmd[0] == 'r') { // 문제 추천
            if (p == 1) { // 최대
                while (curL[maxH[1].id] * -1 != (int)(maxH[1].val / 1000000)) pop(maxH, &maxS); // 아래 제거에서 0으로 만든애들
                printf("%d\n", maxH[1].id);
            } else { // 최소
                while (curL[minH[1].id] != (int)(minH[1].val / 1000000)) pop(minH, &minS); // 정리 후 최대/최소 출력
                printf("%d\n", minH[1].id);
            }
        } else curL[p] = 0; // 제거 
    }
    return 0;
}
