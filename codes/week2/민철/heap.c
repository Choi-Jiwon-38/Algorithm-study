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
