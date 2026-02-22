#include <bits/stdc++.h>

using namespace std;

pair<int, int> mat[500];
int memo[500][500];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int n;
    cin >> n;
    for (int i=0; i<n; i++)
    {
        int r, c;
        cin >> r >> c;
        mat[i] = make_pair(r, c);
    }

    for (int i=1; i<n; i++)
    {
        for (int j=0; j<n-i; j++)
        {
            int k = i + j;
            if (i == 1)
            {
                memo[j][k] = mat[j].first * mat[k].first * mat[k].second;
            }
            else
            {
                memo[j][k] = INT_MAX;
                for (int l=j; l<k; l++)
                    memo[j][k] = min(memo[j][k], memo[j][l] + memo[l+1][k] + (mat[j].first * mat[l].second * mat[k].second));
            }
        }
    }
    cout << memo[0][n-1];
}