#include <stdio.h>
#include <stdlib.h>

// 내림차순 정렬용 비교 함수
int compare(const void *a, const void *b) {
    long long n1 = *(long long *)a;
    long long n2 = *(long long *)b;
    if (n1 < n2) return 1;
    if (n1 > n2) return -1;
    return 0;
}

long long drinks[100001];

int main() {
    char buf[64];
    fgets(buf, 64, stdin);
    int n = atoi(buf); // 음료 개수

    fgets(buf, 64, stdin); // 음료 양들 한꺼번에 읽기 어려우니 sscanf 반복이나 별도 처리
    char *ptr = buf;
    for (int i = 0; i < n; i++) {
        scanf("%lld", &drinks[i]); 
    }

    qsort(drinks, n, sizeof(long long), compare); // 내림차순 정렬

    double res = (double)drinks[0]; // 가장 큰 놈은 그냥 더하기
    for (int i = 1; i < n; i++) {
        res += (double)drinks[i] / 2.0; // 나머지는 /2 해서 더하기
    }

    printf("%g\n", res); // 소수점 생각하기
    return 0;
}
