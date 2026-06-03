#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int prev_num = nums[0], ret = 1;
        for (int i=1; i<nums.size(); i++) {
            int num = nums[i];

            if (prev_num == num) {
                nums[i] = INT_MAX;
            }
            else {
                prev_num = nums[i];
                ret++;
            }
        }

        sort(nums.begin(), nums.end());
        return ret;
    }
};