#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int lsum = 0, rsum = 0;
        for (int i=1; i<nums.size(); i++)
            rsum += nums[i];

        int idx = 0;
        while (lsum != rsum && idx < nums.size() - 1) {
            lsum += nums[idx];
            rsum -= nums[idx + 1];
            idx++;
        }
        return (idx == (nums.size() - 1) ? -1 : idx);
    }
};