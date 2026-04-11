#include <bits/stdc++.h>

using namespace std;

int nums[100000];
int memo[100000];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, ans = INT_MIN;
    cin >> N;
    for (int i=0; i<N; i++) {
        int c;
        cin >> c;
        nums[i] = c;
    }

    memo[0] = nums[0];
    for (int i=1; i<N; i++)
        memo[i] = max(memo[i-1], nums[i-1]) + nums[i];
    
    for (int i=0; i<N; i++)
        ans = max(ans, max(memo[i], nums[i]));

    cout << ans;
}