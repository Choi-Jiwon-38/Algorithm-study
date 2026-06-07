#include <bits/stdc++.h>

using namespace std;

class Solution {
    int cnt[1001];
public:
    int hIndex(vector<int>& citations) {
        for (int c: citations)
            cnt[c]++;

        int s = 0;
        for (int i=1000; i>0; i--) {
            s += cnt[i];
            cnt[i] = s;
        }

        for (int i=1000; i>0; i--) {
            if (cnt[i] >= i)
                return i;
        }
        return 0;
    }
};