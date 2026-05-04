#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ret;

        sort(nums.begin(), nums.end());

        const int sz = nums.size();
        for (int i=0; i<sz; i++) {
            if (i > 0 && nums[i] == nums[i-1])
                continue;

            int j = i + 1, k = sz - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == 0) {
                    ret.push_back({nums[i], nums[j], nums[k]});
                    j++;
                    k--;

                    while (j < k && nums[j] == nums[j-1])
                        j++;
                    while (j < k && nums[k] == nums[k + 1])
                        k--;
                }
                else {
                    if (sum < 0)
                        j++;
                    else
                        k--;
                }
            }
        }

        return ret;
    }
};