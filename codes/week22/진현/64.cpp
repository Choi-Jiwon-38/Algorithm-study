#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    #define y(p) (p.first)
    #define x(p) (p.second)
    typedef pair<int, int> point;

    int N, M;
    int memo[200][200];
    point dk[2] = {{0, 1}, {1, 0}};

    void dfs(vector<vector<int>>& grid, point p, int _val) {
        memo[y(p)][x(p)] = _val;

        for (auto [dy, dx]: dk) {
            int ny = y(p) + dy, nx = x(p) + dx;
            if (ny < N && nx < M) {
                int val = _val + grid[ny][nx];
                if (val < memo[ny][nx])
                    dfs(grid, {ny, nx}, val);
            }
        }
    }

    int minPathSum(vector<vector<int>>& grid) {
        N = grid.size();
        M = grid[0].size();
        for (int i=0; i<N; i++)
            for (int j=0; j<M; j++)
                memo[i][j] = INT_MAX;

        dfs(grid, {0, 0}, grid[0][0]);
        return memo[N-1][M-1];
    }
};