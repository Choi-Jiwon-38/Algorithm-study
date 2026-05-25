#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int ret = 0, altitude = 0;
        for (auto g: gain) {
            altitude += g;
            ret = max(ret, altitude);
        }
        return ret;
    }
};