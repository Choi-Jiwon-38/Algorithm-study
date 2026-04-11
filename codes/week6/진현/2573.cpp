#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> point;
typedef pair<point, int> ppi;

#define x(p) (p.second)
#define y(p) (p.first)

int N, M;
int ice[300][300];
bool visited[300][300];
point dk[4] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

void dfs(point p, queue<point>& q, int& nr_ice) {
    visited[y(p)][x(p)] = true;
    if (!ice[y(p)][x(p)])
        return;
    
    q.push(p);
    nr_ice++;
    for (auto [dy, dx]: dk) {
        int nx = dx + x(p), ny = dy + y(p);
        if ((0 < nx && nx < M) && (0 < ny && ny < N) \
            && (ice[ny][nx] > 0) && !visited[ny][nx])
            dfs(make_pair(ny, nx), q, nr_ice);
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    bool is_saved = false;
    int ans = 0, g = 0;
    point init_p;
    queue<point> tg_q;
    queue<ppi> lazy_q;
    cin >> N >> M;
    for (int i=0; i<N ;i++) {
        for (int j=0; j<M; j++) {
            cin >> ice[i][j];

            if (!is_saved && ice[i][j] > 0) {
                is_saved = true;
                init_p = make_pair(i, j);
            }
        }
    }
    
    dfs(init_p, tg_q, g);
    // step
    while (1) {
        int nr_ice = 0, chunked_nr_ice = 0;
        is_saved = false;

        // 빙산 녹이기
        while (!tg_q.empty()) {
            int nr_seawater = 0;
            point p = tg_q.front();
            tg_q.pop();

            for (auto [dy, dx]: dk) {
                int nx = dx + x(p), ny = dy + y(p);
                if (!ice[ny][nx])
                    nr_seawater++;
            }

            int n_ice = ice[y(p)][x(p)] - nr_seawater;
            if (n_ice > 0) {
                nr_ice++;

                if (!is_saved) {
                    is_saved = true;
                    init_p = p;
                }
            }
            else {
                n_ice = 0;
            }
            lazy_q.push(make_pair(p, n_ice));
        }

        // 빙산 맵 갱신
        while (!lazy_q.empty()) {
            point p = lazy_q.front().first;
            int n_ice = lazy_q.front().second;
            lazy_q.pop();

            ice[y(p)][x(p)] = n_ice;
        }

        // 빙산 개수 확인
        ans++;
        memset(visited, false, sizeof(visited));
        dfs(init_p, tg_q, chunked_nr_ice);
        if (nr_ice != chunked_nr_ice) {
            break;
        }
        else if (nr_ice == 0) {
            ans = 0;
            break;
        }
    }

    cout << ans;
}