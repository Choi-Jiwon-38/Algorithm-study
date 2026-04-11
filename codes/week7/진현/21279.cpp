#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

#define get_root(tree) (tree[1])

struct SegTree {
    // y좌표 값으로 인덱싱
    ll tree[400005];
    int cnt_tree[400005];
    int y_ed;

    void init(int max_y) {
        y_ed = max_y;
    }

    void update(int node, int t_st, int t_ed, int t_idx, int val) {
        // out of range
        if (t_idx < t_st || t_idx > t_ed)
            return;
        
        // 리프 노드
        if (t_st == t_ed) {
            tree[node] += val;
            if (val > 0)
                cnt_tree[node]++;
            else
                cnt_tree[node]--;
            return;
        }

        int mid = (t_st + t_ed) >> 1;
        int l = node * 2, r = l + 1;

        update(l, t_st, mid, t_idx, val);
        update(r, mid + 1, t_ed, t_idx, val);
        tree[node] = tree[l] + tree[r];
        cnt_tree[node] = cnt_tree[l] + cnt_tree[r];
    }
};

vector<pii> x_vec[100001]; // x -> y, v
vector<pii> y_vec[100001]; // y -> x, v

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, C, max_x = -1, max_y = -1;
    ll ans = 0;
    SegTree seg_tree;

    cin >> N >> C;
    for (int i=0; i<N; i++) {
        int x, y, v;
        cin >> x >> y >> v;

        x_vec[x].emplace_back(y, v);
        y_vec[y].emplace_back(x, v);
        max_x = max(max_x, x);
        max_y = max(max_y, y);
    }
    seg_tree.init(max_y);

    // x 좌표를 늘려가면서 광물 추가
    for (int x=0; x<=max_x; x++) {
        for (auto [y, v]: x_vec[x]) {
            if (y <= seg_tree.y_ed)
                seg_tree.update(1, 0, seg_tree.y_ed, y, v);
        }

        // 트리의 광물 삭제
        while (get_root(seg_tree.cnt_tree) > C) {
            for (auto [tg_x, v]: y_vec[seg_tree.y_ed]) {
                if (tg_x <= x)
                    seg_tree.update(1, 0, seg_tree.y_ed, seg_tree.y_ed, -v);
            }
            seg_tree.y_ed--;
        }

        ans = max(ans, get_root(seg_tree.tree));
    }

    cout << ans;
}