#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

constexpr ll min_i = 1, max_i = INT_MAX;
int N, C;
int coord[200000];

bool check(ll d) {
    int idx = 0, w_cnt = 1;

    for (; idx<N;) {
        int tg = idx + 1;
        bool found = false;

        while (tg < N) {
            int dist = abs(coord[idx] - coord[tg]);

            if (dist >= d) {
                idx = tg;
                w_cnt++;
                found = true;
                break;
            }
            else {
                tg++;
            }
        }

        if (w_cnt >= C || !found)
            break;
    }

    return w_cnt >= C;
}

ll para_search() {
    ll l = min_i, r = max_i;
    ll ans = min_i;

    while (l <= r) {
        ll mid = l + ((r - l) >> 1);
        if (check(mid)) {
            l = mid + 1;
            ans = mid;
        }
        else {
            r = mid - 1;
        }
    }

    return ans;
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    cin >> N >> C;
    for (int i=0; i<N; i++)
        cin >> coord[i];

    sort(begin(coord), begin(coord) + N);
    ll ans = para_search();
    cout << ans;
}