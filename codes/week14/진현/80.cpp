#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int tg = 10001, cnt = 1, ret = 0; 
        auto it = nums.begin();
        for (; it!=nums.end(); it++) {
            if (tg == *it) {
                cnt++;

                if (cnt > 2)
                    *it = INT_MAX;
                else
                    ret++;
            }
            else {
                tg = *it;
                cnt = 1;
                ret++;
            }
        }

        sort(nums.begin(), nums.end());
        return ret;
    }
};