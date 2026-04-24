#include <bits/stdc++.h>

using namespace std;


class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max_c = -1;
        vector<bool> ret;

        for (int c: candies) {
            if (max_c < c)
                max_c = c;
        }

        for (int c: candies) {
            if (c + extraCandies >= max_c)
                ret.push_back(true);
            else
                ret.push_back(false);
        }

        return ret;
    }
};