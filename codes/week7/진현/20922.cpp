#include <bits/stdc++.h>

using namespace std;

int nums[200000];
int cnts[100001];
int N, K, st, ed, tg, sz, ans;

void szup() {
    if (ed >= N)
        return;
    
    while (ed < N) {
        tg = nums[ed];
        if (cnts[tg] + 1 > K)
            return;

        cnts[tg]++;
        sz++;
        ed++;
    }
}

void szdown() {
    if (ed >= N)
        return;
    
    while (st < ed) {
        int cur = nums[st];
        cnts[cur]--;
        sz--;
        st++;

        if (cur == tg) 
            return;
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    cin >> N >> K;
    for (int i=0; i<N; i++)
        cin >> nums[i];
    
    while (ed < N) {
        szup();
        ans = max(ans, sz);
        szdown();
    }
    cout << ans;
}