#include <bits/stdc++.h>

using namespace std;

vector<int> graph[10001];
bool visited[10001];


int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, M, max_val;
    vector<int> ans;
    cin >> N >> M;
    for (int i=0; i<M; i++) {
        int v1, v2;
        cin >> v1 >> v2;
        graph[v2].push_back(v1);
    }

    for (int i=1; i<=N; i++) {
        int vnum = 0;
        queue<int> q;
        memset(visited, false, sizeof(bool) * (1 + N));

        q.push(i);
        visited[i] = true;
        while (!q.empty()) {
            int tg = q.front();
            q.pop();
            vnum++;

            for (auto v: graph[tg]) {
                if (!visited[v]) {
                    visited[v] = true;
                    q.push(v);
                }
            }
        }

        if (vnum > max_val) {
            ans.clear();
            max_val = vnum;
            ans.push_back(i);
        }
        else if (vnum == max_val) {
            ans.push_back(i);
        }
    }

    for (auto v: ans)
        cout << v << ' ';
}