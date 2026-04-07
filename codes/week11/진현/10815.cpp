#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, M;
    cin >> N;
    unordered_set<int> us;

    for (int i=0; i<N; i++) {
        int c;
        cin >> c;
        us.insert(c);
    }

    cin >> M;
    while (M--) {
        int q;
        cin >> q;
        
        if (us.find(q) != us.end())
            cout << 1 << ' ';
        else
            cout << 0 << ' ';
    }
}