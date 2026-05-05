#include <bits/stdc++.h>

using namespace std;

int N, M;

void dfs(vector<int>& v) {
    if (v.size() >= M) {
        for (int i: v)
            cout << i << ' ';
        cout << '\n';
        return;
    }

    for (int i=1; i<=N; i++) {
        if (find(v.begin(), v.end(), i) == v.end()) {
            v.push_back(i);
            dfs(v);
            v.pop_back();
        }
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    cin >> N >> M;
    vector<int> v;
    dfs(v);

    return 0;
}