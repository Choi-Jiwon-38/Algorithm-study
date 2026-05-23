#include <bits/stdc++.h>

using namespace std;

class Solution {
    typedef pair<int, int> point;

    int m, n;
    int board[101][101];
    point dv[2] = {{1, 0}, {0, 1}};
public:

    void dfs(point p) {
        int &y = p.first, &x = p.second;

        if (x > 1 && board[y][x-1] == 0)
            return;
        else if (y > 1 && board[y-1][x] == 0)
            return;
        
        board[y][x] = board[y-1][x] + board[y][x-1];
        for (auto [dy, dx]: dv) {
            int ny = y + dy, nx = x + dx;
            if (ny <= m && nx <= n)
                dfs({ny, nx});
        }
    }

    int uniquePaths(int _m, int _n) {
        m = _m;
        n = _n;

        board[1][1] = 1;
        dfs({1, 2});
        dfs({2, 1});

        return board[m][n];
    }
};