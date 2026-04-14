#include <bits/stdc++.h>

using namespace std;

struct egg {
    int durab, weight;
};

int N, ans = 0;
vector<egg> v;

inline int count_egg() {
    int cnt = 0;
    for (auto e: v) {
        if (e.durab <= 0)
            cnt++;
    }
    return cnt;
}

void dfs(int idx) {
    if (idx == N) {
        ans = max(ans, count_egg());
        return;
    }
    else if (v[idx].durab <= 0) {
        dfs(idx + 1);
        return;
    }

    bool is_last_egg = true;
    for (int i=0; i<N; i++) {
        if (i != idx && v[i].durab > 0) {
            is_last_egg = false;
            v[i].durab -= v[idx].weight;
            v[idx].durab -= v[i].weight;

            dfs(idx + 1);

            v[i].durab += v[idx].weight;
            v[idx].durab += v[i].weight;
        }
    }

    if (is_last_egg)
        dfs(idx + 1);
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    cin >> N;
    for (int i=0; i<N; i++) {
        int d, w;
        cin >> d >> w;
        v.push_back({d, w});
    }

    dfs(0);
    cout << ans;
    return 0;
}