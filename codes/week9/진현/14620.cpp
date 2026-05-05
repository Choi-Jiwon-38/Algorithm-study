#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

#define MAX_C (200 * 5 * 3)

int N;
int costs[10][10], f_costs[10][10];
bool flowers[10][10];
pii dv[5] = {{0, 0}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}};

inline int get_cost(int y, int x) {
    int c = 0;
    for (auto [dy, dx]: dv)
        c += costs[y + dy][x + dx];
    return c;
}

bool set_flower(int y, int x, bool val) {
    if (val) {
        for (auto [dy, dx] : dv) {
            int ny = y + dy, nx = x + dx;

            if (flowers[ny][nx])
                return false;
        }

        for (auto [dy, dx] : dv) {
            int ny = y + dy, nx = x + dx;

            flowers[ny][nx] = true;
        }
    }
    else {
        for (auto [dy, dx] : dv) {
            int ny = y + dy, nx = x + dx;

            flowers[ny][nx] = false;
        }
    }

    return true;
}

int test_cost(int depth) {
    int min_c = MAX_C;

    for (int i=1; i<N-1; i++) {
        for (int j=1; j<N-1; j++) {
            if (!set_flower(i, j, true)) {
                continue;
            }
            else {
                if (depth < 2)
                    min_c = min(min_c, f_costs[i][j] + test_cost(depth + 1));
                else
                    min_c = min(min_c, f_costs[i][j]);
            }

            set_flower(i, j, false);
        }
    }

    return min_c;
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    cin >> N;
    for (int i=0; i<N; i++)
        for (int j=0; j<N; j++)
            cin >> costs[i][j];
    
    for (int i=1; i<N-1; i++)
        for (int j=1; j<N-1; j++)
            f_costs[i][j] = get_cost(i, j);

    cout << test_cost(0);
}