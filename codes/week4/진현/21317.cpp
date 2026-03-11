#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

pii powers[20];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, K, ans = INT_MAX;
    vector<pii> q[20];
    cin >> N;
    for (int i=0; i<N-1; i++) {
        int c1, c2;
        cin >> c1 >> c2;
        powers[i] = make_pair(c1, c2);
    }
    cin >> K;

    q[0].push_back(make_pair(0, 0));
    for (int i=0; i<N-1; i++) {
        vector<pii>& queue = q[i];
        while (!queue.empty()) {
            pii& tg = queue.back();
            // small
            q[i + 1].push_back(make_pair(tg.first + powers[i].first, tg.second));
            // big
            if (i + 2 < N)
                q[i + 2].push_back(make_pair(tg.first + powers[i].second, tg.second));
            // so big
            if (!tg.second && i + 3 < N)
                q[i + 3].push_back(make_pair(tg.first + K, 1));
            queue.pop_back();
        }
    }

    vector<pii>& queue = q[N - 1];
    while (!queue.empty()) {
        ans = min(ans, queue.back().first);
        queue.pop_back();
    }
    cout << ans;
}