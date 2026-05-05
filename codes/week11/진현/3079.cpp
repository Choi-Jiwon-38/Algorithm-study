#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

const ll min_tm = 1, max_tm = LLONG_MAX;
int N, M;
int im_time[100000];

bool check(ll t) {
    ll p_cnt = 0;
    for (int i=0; i<N; i++) {
        p_cnt += (t / im_time[i]);

        if (p_cnt >= M)
            break;
    }

    if (p_cnt >= M)
        return true;
    else
        return false;
}

ll para_search() {
    ll l = min_tm, r = max_tm;
    ll ans = max_tm;

    while (l <= r) {
        ll mid = l + ((r - l) >> 1);

        if (check(mid)) {
            r = mid - 1;
            ans = mid;
        }
        else {
            l = mid + 1;
        }
    }

    return ans;
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);
    
    cin >> N >> M;
    for (int i=0; i<N; i++)
        cin >> im_time[i];

    ll ans = para_search();
    cout << ans;
}