#include <bits/stdc++.h>

using namespace std;

int land[25][25];
bool check[25][25];
int n, rst;
priority_queue<int, vector<int>, greater<int>> ans;
vector<pair<int, int>> dk;

void dfs(int i, int j)
{
    rst++;
    check[i][j] = true;

    for (auto [di, dj]: dk)
    {
        int n_i = i + di, n_j = j + dj;
        if ((0 <= n_i && n_i < n) && (0 <= n_j && n_j < n))
        {
            if (land[n_i][n_j] == 1 && !check[n_i][n_j])
            {
                dfs(n_i, n_j);
            }
        }
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);
    dk.emplace_back(1, 0); dk.emplace_back(-1, 0);
    dk.emplace_back(0, 1); dk.emplace_back(0, -1);

    cin >> n;
    for (int i=0; i<n; i++)
    {
        int j = 0;
        string s;
        cin >> s;
        for (auto c: s)
            land[i][j++] = c - '0';
    }

    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
        {
            if (land[i][j] == 1 && !check[i][j])
            {
                rst = 0;
                dfs(i, j);
                ans.push(rst);
            }
        }
    }

    cout << ans.size() << '\n';
    while (!ans.empty())
    {
        cout << ans.top() << '\n';
        ans.pop();
    }
}