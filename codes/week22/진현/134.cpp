#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int gsum = 0, csum = 0, cur_gas = 0, st_idx = 0;
        for (int i=0; i<gas.size(); i++) {
            gsum += gas[i];
            csum += cost[i];

            cur_gas += gas[i] - cost[i];

            if (cur_gas < 0) {
                st_idx = i + 1;
                cur_gas = 0;
            }
        }

        if (gsum < csum)
            return -1;
        else
            return st_idx;
    }
};