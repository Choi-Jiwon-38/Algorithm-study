#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

const ll min_i = 1, max_i = INT_MAX;
int K, N;
int lan[10000];

bool check(ll t) {
    ll t_n = 0;
    for (int i=0; i<K; i++)
        t_n += lan[i] / t;
    
    return t_n >= N;
}

ll para_search() {
    ll l = min_i, r = max_i;
    ll ans = l;
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

    cin >> K >> N;
    for (int i=0; i<K; i++)
        cin >> lan[i];

    ll ans = para_search();
    cout << ans;
}