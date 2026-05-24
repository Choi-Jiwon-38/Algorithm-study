#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int reverseBits(int n) {
        unsigned int ret = 0, mask = 1;

        for (int i=0; i<32; i++) {
            ret >>= 1;
            if (n & mask)
                ret |= (1 << 31);

            mask <<= 1;
        }

        return ret;
    }
};