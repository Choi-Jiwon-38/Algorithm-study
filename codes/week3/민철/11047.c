#include <stdio.h>
#include <stdlib.h>

int coins[11];

int main() {
    char buf[64];
    int n, k;
    fgets(buf, 64, stdin);
    sscanf(buf, "%d %d", &n, &k); // 동전 종류 n, 목표 금액 k

    for (int i = 0; i < n; i++) {
        fgets(buf, 64, stdin);
        coins[i] = atoi(buf); // 동전 가치
    }

    int count = 0;
    // 가장 큰 값부터(인덱스 n-1부터) 역순으로 확인
    for (int i = n - 1; i >= 0; i--) {
        if (k == 0) break;
        if (coins[i] <= k) { // 뺄 수 있는가? -> yes
            count += k / coins[i]; // 나눠서 개수 바로 더하기
            k %= coins[i]; // 남은 금액 갱신
        }
    }

    printf("%d\n", count);
    return 0;
}
