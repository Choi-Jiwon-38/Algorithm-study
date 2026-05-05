#include <bits/stdc++.h>

using namespace std;

int rains[500];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int H, W, st_idx = -1, ed_idx = -1, r_blk = 0;
    cin >> H >> W;
    for (int i=0; i<W; i++) {
        cin >> rains[i];
        if (st_idx < 0 && rains[i] > 0)
            st_idx = i;
    }

    int idx = st_idx;
    while (st_idx < W - 1) {
        int ed_idx = W - 1, loc_max = -1;
        for (int idx=ed_idx; idx>st_idx; idx--) {
            if (rains[st_idx] <= rains[idx]) {
                loc_max = rains[idx];
                ed_idx = idx;
            }
            else if (rains[idx] >= loc_max) {
                loc_max = rains[idx];
                ed_idx = idx;
            }
        }

        int base_blk = min(rains[st_idx], rains[ed_idx]);
        for (int i=st_idx+1; i<ed_idx; i++) {
            r_blk += (base_blk - rains[i]);
        }
        st_idx = ed_idx;
    }

    cout << r_blk;
}