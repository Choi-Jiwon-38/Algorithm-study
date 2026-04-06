#include <bits/stdc++.h>

using namespace std;

int N, min_ans = INT_MAX, max_ans = INT_MIN;
int nums[11];

struct _ops {
    int add, m_add, mul, div;

    int count() {
        return add + m_add + mul + div;
    }
} ops;

void dfs(int k, int idx) {
    if (ops.count() == 0) {
        min_ans = min(min_ans, k);
        max_ans = max(max_ans, k);
        return;
    }

    if (ops.add) {
        ops.add--;
        dfs(k + (nums[idx]), idx + 1);
        ops.add++;
    }
    if (ops.m_add) {
        ops.m_add--;
        dfs(k - (nums[idx]), idx + 1);
        ops.m_add++;
    }
    if (ops.mul) {
        ops.mul--;
        dfs(k * (nums[idx]), idx + 1);
        ops.mul++;
    }
    if (ops.div) {
        ops.div--;
        dfs(k / (nums[idx]), idx + 1);
        ops.div++;
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    cin >> N;
    for (int i=0; i<N; i++)
        cin >> nums[i];
    
    cin >> ops.add >> ops.m_add >> ops.mul >> ops.div;
    dfs(nums[0], 1);
    cout << max_ans << '\n' << min_ans;
    return 0;
}