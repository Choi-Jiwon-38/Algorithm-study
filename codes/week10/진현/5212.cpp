    #include <bits/stdc++.h>

    using namespace std;
    typedef pair<int, int> point;

    char e_map[10][10], af_map[10][10];
    point dv[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    int main(void)
    {
        cin.tie(NULL);
        cout.tie(NULL);
        iostream::sync_with_stdio(false);

        int R, C;
        cin >> R >> C;
        for (int i=0; i<R; i++)
            for (int j=0; j<C; j++)
                cin >> e_map[i][j];
        
        int i_st = R, i_ed = 0, j_st = C, j_ed = 0;
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (e_map[i][j] == '.') {
                    af_map[i][j] = '.';
                    continue;
                }

                int w_cnt = 0;
                for (auto [di, dj]: dv) {
                    int ni = i + di, nj = j + dj;
                    if ((0 <= ni && ni < R) && (0 <= nj && nj < C)) {
                        if (e_map[ni][nj] == '.')
                            w_cnt++;
                    }
                    else {
                        w_cnt++;
                    }
                }

                if (w_cnt >= 3) {
                    af_map[i][j] = '.';
                }
                else {
                    af_map[i][j] = 'X';

                    i_st = min(i_st, i);
                    i_ed = max(i_ed, i);
                    j_st = min(j_st, j);
                    j_ed = max(j_ed, j);
                }
            }
        }

        for (int i=i_st; i<=i_ed; i++) {
            for (int j=j_st; j<=j_ed; j++)
                cout << af_map[i][j];
            cout << '\n';
        }
    }