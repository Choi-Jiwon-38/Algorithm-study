#include <bits/stdc++.h>

using namespace std;

int shshi[3000000];
int cnts[3001];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);
    int N, d, k, c, max_ks = 0, kinds = 1;
    cin >> N >> d >> k >> c;
    cnts[c]++;
    for (int i=0; i<N; i++)
        cin >> shshi[i];
    for (int i=0; i<k; i++) {
        int &tg = shshi[i];
        if (cnts[tg] == 0)
            kinds++;
        cnts[tg]++;
    }
    // corner case
    if (N == k) {
        cout << kinds;
        return 0;
    }

    max_ks = kinds;
    for (int i=0; i<N; i++) {
        int& st_tg = shshi[i];
        int& ed_tg = shshi[(i + k) % N];
        cnts[st_tg]--;
        cnts[ed_tg]++;

        if (cnts[st_tg] == 0)
            kinds--;
        if (st_tg != ed_tg && cnts[ed_tg] == 1)
            kinds++;
        max_ks = max(max_ks, kinds);
    }
    cout << max_ks;
}