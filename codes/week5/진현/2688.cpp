#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

ll memo[65][10];
ll ans[65];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    for (int i=0; i<10; i++)
        memo[1][i] = 1;

    for (int i=1; i<=64; i++) {
        for (int j=0; j<10; j++) {
            for (int k=0; k<=j; k++) {
                memo[i][j] += memo[i - 1][k];
            }

            ans[i] += memo[i][j];
        }
    }

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        cout << ans[n] << '\n';
    }
}