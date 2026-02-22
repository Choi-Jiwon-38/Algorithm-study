#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> point;

#define x(p) (p.second)
#define y(p) (p.first)

int n, m;
int board[500][500];
int memo[500][500];
vector<point> dv;

void dfs(const point& p) {
    if (memo[y(p)][x(p)] != 0)
        return;

    for (int t=0; t<4; t++) {
        int nx = x(p) + x(dv[t]), ny = y(p) + y(dv[t]);
        if ((0 <= nx && nx < m) && (0 <= ny && ny < n) \
            && (board[ny][nx] < board[y(p)][x(p)])) {
            dfs(make_pair(ny, nx));
            if (memo[ny][nx] > 0)
                memo[y(p)][x(p)] += memo[ny][nx];
        }
    }
    if (memo[y(p)][x(p)] == 0)
        memo[y(p)][x(p)] = -1;
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    // E, W, S, N
    dv.push_back(make_pair(0, 1)); 
    dv.push_back(make_pair(0, -1));
    dv.push_back(make_pair(1, 0)); 
    dv.push_back(make_pair(-1, 0));

    cin >> n >> m;
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            int c;
            cin >> c;
            board[i][j] = c;
        }
    }

    // corner case
    if (n == 1 && m == 1) {
        cout << 1;
        return 0;
    }

    memo[n - 1][m - 1] = 1;
    if (board[0][1] < board[0][0])
        dfs(make_pair(0, 1));
    if (board[1][0] < board[0][0])
        dfs(make_pair(1, 0));
    
    int H = 0;
    H += (memo[0][1] < 0 ? 0 : memo[0][1]);
    H += (memo[1][0] < 0 ? 0 : memo[1][0]);
    cout << H;
    return 0;
}