#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int h = nums.size() / 2 + 1;

        sort(nums.begin(), nums.end());

        int cnt = 0, tg = INT_MIN;
        for (auto k: nums) {
            if (tg != k) {
                tg = k;
                cnt = 1;
            }
            else {
                cnt++;

                if (cnt >= h)
                    break;
            }
        }

        return tg;
    }
};