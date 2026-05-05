#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> point;

int N, H, D;

struct p_status {
    int step;
    int shield;
    int total_hp;

    void init(int H, bool is_start) {
        step = is_start ? -1 : 0;
        shield = 0;
        total_hp = is_start ? H + 1 : H;
    }
};

struct map_status {
    int hp;
    bool is_safe;
    bool is_shield;

    void init(char ch) {
        if (ch == 'U')
            is_shield = true;
        else
            is_shield = false;

        if (ch == 'E')
            is_safe = true;
        else
            is_safe = false;

        hp = -1;
    }
};

p_status play_map[500][500];
map_status rain_map[500][500];
point dv[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    point st_p, ed_p;
    cin >> N >> H >> D;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            char ch;
            cin >> ch;
            play_map[i][j].init(0, false);
            rain_map[i][j].init(ch);

            if (ch == 'S')
                st_p = {i, j};
            else if (ch == 'E')
                ed_p = {i, j};
        }
    }

    p_status& st_stat = play_map[st_p.first][st_p.second];
    map_status &st_map = rain_map[st_p.first][st_p.second];
    st_stat.init(H, true);
    st_map.hp = H;

    // bfs
    queue<pair<point, p_status&>> q;
    q.emplace(st_p, st_stat);
    while (q.size()) {
        point p = q.front().first;
        p_status& bf_stat = q.front().second;
        q.pop();

        int& y = p.first, &x = p.second;
        p_status& cur_stat = play_map[y][x];
        map_status &cur_map = rain_map[y][x];

        // 2.
        if (cur_map.is_safe) {
            cout << bf_stat.step + 1;
            return 0;
        }

        cur_stat.step = bf_stat.step + 1;
        // 3.
        if (cur_map.is_shield) {
            cur_stat.shield = D - 1;
            cur_stat.total_hp = (bf_stat.total_hp - bf_stat.shield) + D - 1;
        }
        // 4.
        else if (bf_stat.shield) {
            cur_stat.shield = bf_stat.shield - 1;
            cur_stat.total_hp = bf_stat.total_hp - 1;
        }
        else {
            cur_stat.total_hp = bf_stat.total_hp - 1;
        }
        // 5~6.
        if (cur_stat.total_hp <= 0)
            continue;

        for (auto [dy, dx]: dv) {
            int ny = y + dy, nx = x + dx;
            if ((0 <= nx && nx < N) && (0 <= ny && ny < N)) {
                p_status &next_stat = play_map[ny][nx];
                map_status& next_map = rain_map[ny][nx];

                if (cur_stat.total_hp > next_map.hp) {
                    next_map.hp = cur_stat.total_hp;
                    q.emplace(make_pair(ny, nx), cur_stat);
                }
            }
        }
    }

    // Not found!
    cout << -1;
}