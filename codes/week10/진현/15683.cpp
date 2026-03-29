#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> point;

int N, M, c_idx, ans = 64;
int office[8][8];
point dv[4] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
void (*cctv_fns[5])(int idx, int dir, bool restore);

struct cctv {
    int c_id;
    point p;

    void init(int i, int j) {
        static int _id = 0;
        c_id = _id++;
        p = {i, j};
    }
} cctvs[8];

struct b_element {
    bool is_wall;
    bitset<8> is_checked;
} board[8][8];

inline void clear_map() {
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            board[i][j].is_checked.reset();

            if (office[i][j] == 6)
                board[i][j].is_wall = true;
            else if (office[i][j] != 0)
                board[i][j].is_checked.flip();
        }
    }
}

inline void check_map() {
    int z_cnt = 0;
    for (int i=0; i<N; i++)
        for (int j=0; j<M; j++)
            if (board[i][j].is_checked.to_ulong() == 0 && office[i][j] == 0)
                z_cnt++;
            
    ans = min(ans, z_cnt);
}

inline void check_line(int ny, int nx, int dy, int dx, int id, bool restore) {
    while (1) {
        ny += dy;
        nx += dx;
        if ((0 <= ny && ny < N) && (0 <= nx && nx < M)) {
            if (board[ny][nx].is_wall) {
                break;
            }
            else {
                if (restore)
                    board[ny][nx].is_checked.reset(id);
                else
                    board[ny][nx].is_checked.set(id);
            }
        }
        else {
            break;
        }
    }
}

void check_cctv1(int idx, int dir, bool restore) {
    point &p = cctvs[idx].p;
    int ny = p.first, nx = p.second, id = cctvs[idx].c_id;
    int &dy = dv[dir].first, &dx = dv[dir].second;
    check_line(ny, nx, dy, dx, id, restore);
}

void check_cctv2(int idx, int dir, bool restore) {
    point &p = cctvs[idx].p;
    int id = cctvs[idx].c_id;
    for (int k=0; k<=2; k+=2) {
        int ny = p.first, nx = p.second;
        int &dy = dv[(dir + k) % 4].first, &dx = dv[(dir + k) % 4].second;
        check_line(ny, nx, dy, dx, id, restore);
    }
}

void check_cctv3(int idx, int dir, bool restore) {
    point &p = cctvs[idx].p;
    int id = cctvs[idx].c_id;
    for (int k=0; k<=1; k++) {
        int ny = p.first, nx = p.second;
        int &dy = dv[(dir + k) % 4].first, &dx = dv[(dir + k) % 4].second;
        check_line(ny, nx, dy, dx, id, restore);
    }
}

void check_cctv4(int idx, int dir, bool restore) {
    point &p = cctvs[idx].p;
    int id = cctvs[idx].c_id;
    for (int k=0; k<=2; k++) {
        int ny = p.first, nx = p.second;
        int &dy = dv[(dir + k) % 4].first, &dx = dv[(dir + k) % 4].second;
        check_line(ny, nx, dy, dx, id, restore);
    }
}

void check_cctv5(int idx, bool restore) {
    point& p = cctvs[idx].p;
    int id = cctvs[idx].c_id;
    for (int k=0; k<=3; k++) {
        int ny = p.first, nx = p.second;
        int &dy = dv[k].first, &dx = dv[k].second;
        check_line(ny, nx, dy, dx, id, restore);
    }
}

void sim_cctv(int idx) {
    point& tg = cctvs[idx].p;
    int type = office[tg.first][tg.second];

    if (type == 5) {
        check_cctv5(idx, false);

        if (idx > 0)
            sim_cctv(idx - 1);
        else
            check_map();

        check_cctv5(idx, true);
    }
    else {
        auto check_fn = cctv_fns[type];
        for (int d=0; d<4; d++) {
            check_fn(idx, d, false);

            if (idx > 0)
                sim_cctv(idx - 1);
            else
                check_map();

            check_fn(idx, d, true);
        }
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);
    cctv_fns[1] = check_cctv1;
    cctv_fns[2] = check_cctv2;
    cctv_fns[3] = check_cctv3;
    cctv_fns[4] = check_cctv4;

    int cnt = 0, z_cnt = 0;
    cin >> N >> M;
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin >> office[i][j];

            if (0 < office[i][j] && office[i][j] < 6) {
                cctvs[c_idx++].init(i, j);
            }
            else if (office[i][j] == 0) {
                cnt++;
                z_cnt++;
            }
            else {
                cnt++;
            }
        }
    }

    // cctv가 없는 경우
    if (cnt == N * M) {
        cout << z_cnt;
        return 0;
    }

    clear_map();
    sim_cctv(c_idx - 1);
    cout << ans;
    return 0;
}