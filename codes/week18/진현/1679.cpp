#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int ret = 0;
        unordered_map<int, int> num_map;

        for (auto i: nums)
            num_map[i]++;
        
        for (auto num: nums) {
            int tg = k - num;
            if (tg <= 0)
                continue;
            
            if (num_map[num] > 0 && num_map[tg] > 0) {
                if (tg == num && num_map[num] < 2)
                    continue;

                num_map[num]--;
                num_map[tg]--;
                ret++;
            }
        }

        return ret;
    }
};