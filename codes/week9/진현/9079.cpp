#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

int cnt_h, ans;
bool board[3][3];
int dv[3] = {0, 1, 2};
pii digv[2][3] = {
    {{0, 0}, {1, 1}, {2, 2}},
    {{0, 2}, {1, 1}, {2, 0}}
};

bool set_coins(int i, bool row, bool diagonal) {
    bool ret = false;
    if (diagonal) {
        for (auto [y, x]: digv[i]) {
            board[y][x] = !board[y][x];
            if (board[y][x])
                cnt_h++;
            else
                cnt_h--;
        }

        if (cnt_h == 0 || cnt_h == 9)
            ret = true;
    }
    else {
        for (auto j: dv) {
            if (row) {
                board[j][i] = !board[j][i];
                if (board[j][i])
                    cnt_h++;
                else
                    cnt_h--;
            }
            else {
                board[i][j] = !board[i][j];
                if (board[i][j])
                    cnt_h++;
                else
                    cnt_h--;
            }
        }

        if (cnt_h == 0 || cnt_h == 9)
            ret = true;
    }
    return ret;
}

void dfs(int depth, int memo) {
    int bf_cnt = cnt_h, mask = 1;

    // 대각선
    for (int i=0; i<2; i++) {
        if (set_coins(i, false, true))
            ans = min(ans, depth);
        else if (!(memo & mask))
            dfs(depth + 1, memo | mask);
        
        set_coins(i, false, true);
        mask <<= 1;
    }

    // rows
    for (int i=0; i<3; i++) {
        if (set_coins(i, true, false))
            ans = min(ans, depth);
        else if (!(memo & mask))
            dfs(depth + 1, memo | mask);

        set_coins(i, true, false);
        mask <<= 1;
    }

    // columns
    for (int i=0; i<3; i++) {
        if (set_coins(i, false, false))
            ans = min(ans, depth);
        else if (!(memo & mask))
            dfs(depth + 1, memo | mask);

        set_coins(i, false, false);
        mask <<= 1;
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int T;
    cin >> T;
    while (T--) {
        cnt_h = 0;
        ans = INT_MAX;
        for (int i=0; i<3; i++) {
            for (int j=0; j<3; j++) {
                char ch;
                cin >> ch;

                if (ch == 'H') {
                    cnt_h++;
                    board[i][j] = true;
                }
                else {
                    board[i][j] = false;
                }
            }
        }

        if (cnt_h == 0 || cnt_h == 0) {
            cout << 0 << '\n';
            continue;
        }

        dfs(1, 0);

        if (ans != INT_MAX)
            cout << ans << '\n';
        else
            cout << -1 << '\n';
    }
}