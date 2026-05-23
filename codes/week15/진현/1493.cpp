#include <bits/stdc++.h>

using namespace std;

class Solution {
    int total_cnt[2], cnt[2];
    vector<int> comp_arr;

public:
    int longestSubarray(vector<int>& nums) {
        int idx = 0, prev_num = nums[0];

        // compress array
        while (idx < nums.size()) {
            if (prev_num != nums[idx]) {
                if (prev_num == 0 && cnt[0] > 1)
                    comp_arr.push_back(0);
                else if (prev_num == 1)
                    comp_arr.push_back(cnt[1]);
                
                cnt[prev_num] = 0;
                prev_num = nums[idx];
            }

            total_cnt[prev_num]++;
            cnt[prev_num]++;
            idx++;
        }
        if (cnt[1] > 0)
            comp_arr.push_back(cnt[1]);

        if (comp_arr.size() == 0) {
            return 0;
        }
        else if (comp_arr.size() == 1) {
            if (total_cnt[0] == 0)
                return comp_arr.front() - 1;
            else
                return comp_arr.front();
        }
        else {
            int ret = -1;
            for (int i=0; i<comp_arr.size()-1; i++)
                ret = max(ret, comp_arr[i] + comp_arr[i+1]);
            
            return ret;
        }
    }
};