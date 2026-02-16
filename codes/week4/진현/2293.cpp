#include <bits/stdc++.h>

using namespace std;

int coins[100];
int memo[10001];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int n, k;
    cin >> n >> k;
    for (int i=0; i<n; i++) {
        int c;
        cin >> c;
        coins[i] = c;
    }

    memo[0] = 1;
    for (int i=0; i<n; i++) {
        for (int c=coins[i]; c<=k; c++) {
            memo[c] += memo[c - coins[i]];
        }
    }

    cout << memo[k];
}