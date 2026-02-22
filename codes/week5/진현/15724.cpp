#include <bits/stdc++.h>

using namespace std;

int jujisu[1025][1025];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, M, K;
    cin >> N >> M;
    for (int i=1; i<=N; i++) {
        for (int j=1; j<=M; j++) {
            int c;
            cin >> c;
            jujisu[i][j] = c;

            jujisu[i][j] += jujisu[i][j - 1];
        }
    }

    cin >> K;
    while (K--) {
        int x1, y1, x2, y2, sum = 0;
        cin >> x1 >> y1 >> x2 >> y2;

        for (int x=x1; x<=x2; x++)
            sum += (jujisu[x][y2] - jujisu[x][y1 - 1]);
        
        cout << sum << '\n';
    }
}