#include <bits/stdc++.h>

using namespace std;

int coin[10];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        int c;
        cin >> c;
        coin[i] = c;
    }

    int idx = n - 1, ans = 0;
    while (k != 0)
    {
        while (coin[idx] > k && idx > 0)
            idx--;
        if (idx == 0)
        {
            ans += k;
            break;
        }

        k -= coin[idx];
        ans++;
    }
    cout << ans;
}