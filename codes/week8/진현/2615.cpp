#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;
typedef pii point;

#define MAXN 19

int board[MAXN + 1][MAXN + 1];
bool visited[MAXN + 1][MAXN + 1][4];
set<point> point_sets[MAXN + 1][MAXN + 1][4];
point dv[4][2] = {
    {{0, 1}, {0, -1}},
    {{1, 0}, {-1, 0}},
    {{1, 1}, {-1, -1}},
    {{-1, 1}, {1, -1}}
};

void dfs(const point& p, const int& d, set<point>& pset, int& cnt) {
    const int &i = p.first, &j = p.second;

    cnt++;
    visited[i][j][d] = true;
    pset.insert({j, i});
    for (int k=0; k<2; k++) {
        int ni = i + dv[d][k].first, nj = j + dv[d][k].second;
        if ((0 < ni && ni <= MAXN) && (0 < nj && nj <= MAXN) \
            && !visited[ni][nj][d] && (board[ni][nj] == board[i][j]))
            dfs({ni, nj}, d, pset, cnt);
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    queue<point> q;
    for (int i=1; i<=MAXN; i++) {
        for (int j=1; j<=MAXN; j++) {
            cin >> board[i][j];
            if (board[i][j])
                q.push({i, j});
        }
    }

    bool is_found = false;
    while (!q.empty() && !is_found) {
        point p = q.front();
        q.pop();


        for (int d=0; d<4; d++) {
            int cnt = 0;
            int &i = p.first, &j = p.second;
            set<point>& pset = point_sets[i][j][d];

            if (visited[i][j][d])
                continue;
            
            dfs(p, d, pset, cnt);
            if (cnt == 5) {
                auto iter = pset.begin(); 
                is_found = true;
                cout << board[i][j] << '\n';
                cout << iter->second << ' ' << iter->first;
                break;
            }
        }
    }

    if (!is_found)
        cout << 0;
    return 0;
}