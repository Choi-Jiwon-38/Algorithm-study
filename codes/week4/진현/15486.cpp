#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

#define get_t(x) (x.first)
#define get_p(x) (x.second)

vector<int> memo[1500002];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, wait_max_p = INT_MIN;
    cin >> N;
    for (int i=1; i<=N; i++) {
        int t, p, max_p = INT_MIN;
        cin >> t >> p;

        vector<int>& v = memo[i];
        while (!v.empty()) {
            max_p = max(max_p, v.back());
            v.pop_back();
        }
        if (wait_max_p >= max_p)
            max_p = wait_max_p;
        else
            wait_max_p = max_p;

        if (i + t <= N + 1)
            memo[i + t].push_back(max(max_p, 0) + p);
        else
            memo[N + 1].push_back(max(max_p, 0));
    }

    int ans = INT_MIN;
    for (auto i: memo[N + 1])
        ans = max(ans, i);
    cout << ans;
}