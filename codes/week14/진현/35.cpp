#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int binary_search(vector<int>& v, int sz, int tg) {
        int st = 0, ed = sz - 1;

        int mid;
        while (st <= ed) {
            mid = (st + ed) >> 1;

            if (v[mid] == tg)
                return mid;
            else if (v[mid] > tg)
                ed = mid - 1;
            else
                st = mid + 1;
        }

        return st;
    }

    int searchInsert(vector<int>& nums, int target) {
        return binary_search(nums, nums.size(), target);
    }
};