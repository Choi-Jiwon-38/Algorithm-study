#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int hammingWeight(int _n) {
        int n = _n, ret = 0;
        while (n > 0) {
            if (n & 1)
                ret++;
            n >>= 1;
        }
        return ret;
    }
};