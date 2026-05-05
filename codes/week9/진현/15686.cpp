#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> point;

#define get_dist(p1, p2) (abs(p1.first - p2.first) + abs(p1.second - p2.second))

int N, M, ppl_cnt, chick_cnt;
int dist_arr[13][100];
int min_arr[100];
point ppls[100];
point chicks[13];
priority_queue<int> pq;
bitset<13> choice;

int min_dist() {
    fill(min_arr, min_arr + ppl_cnt, INT_MAX);

    for (int i=0; i<chick_cnt; i++) {
        if (!choice[i])
            continue;
        
        for (int j=0; j<ppl_cnt; j++)
            min_arr[j] = min(min_arr[j], dist_arr[i][j]);
    }

    int ret = 0;
    for (int i=0; i<ppl_cnt; i++)
        ret += min_arr[i];
    return ret;
}

void dfs(int st_idx) {
    if (choice.count() >= M) {
        int sum = min_dist();
        pq.push(-sum);
        return;
    }

    for (int i=st_idx; i<chick_cnt; i++) {
        choice[i] = 1;
        dfs(i + 1);
        choice[i] = 0;
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    cin >> N >> M;
    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            int inp;
            cin >> inp;
            if (inp == 1)
                ppls[ppl_cnt++] = {i, j};
            else if (inp == 2)
                chicks[chick_cnt++] = {i, j};
        }
    }

    for (int ck=0; ck<chick_cnt; ck++)
        for (int p=0; p<ppl_cnt; p++)
            dist_arr[ck][p] = get_dist(ppls[p], chicks[ck]);

    dfs(0);
    cout << -pq.top();
} 