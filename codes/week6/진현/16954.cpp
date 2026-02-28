#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> point;

#define x(p) (p.second)
#define y(p) (p.first)

char board[16][8];
point dv[9] = {
    {-1, 0}, {0, 1},
    {1, 1}, {-1, -1},
    {1, -1}, {-1, 1},
    {1, 0}, {0, -1},
    {0, 0}
};

void dfs(point p, int turn, bool& is_success) {
    int n_turn = max(turn - 1, 0);
    if (y(p) == 0 && x(p) == 7) {
        is_success = true;
        return;
    }
    else if (board[y(p) + turn][x(p)] == '#') {
        return;
    }

    for (auto [dy, dx]: dv) {
        int nx = dx + x(p), ny = dy + y(p);
        if ((0 <= nx && nx < 8) && (0 <= ny && ny < 8) && board[ny + turn][nx] != '#') {
            dfs(make_pair(ny, nx), n_turn, is_success);
        
            if (is_success)
                return;
        }
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    bool ans = false;
    for (int i=0; i<8; i++) 
        for (int j=0; j<8; j++)
            cin >> board[8 + i][j];
    
    dfs(make_pair(7, 0), 8, ans);
    cout << (ans ? 1 : 0);
}