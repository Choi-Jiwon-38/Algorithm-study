#include <bits/stdc++.h>

using namespace std;

class Solution {
    unordered_set<int> s;
public:
    bool uniqueOccurrences(vector<int>& arr) {
        bool ret = true;
        sort(arr.begin(), arr.end());

        int prev = arr[0], cnt = 1;
        for (int i=1; i<arr.size(); i++) {
            if (prev != arr[i]) {   
                if (s.find(cnt) != s.end()) {
                    ret = false;
                    break;
                }
                else {
                    s.insert(cnt);

                    prev = arr[i];
                    cnt = 1;
                }
            }
            else {
                cnt++;
            }
        }
        if (s.find(cnt) != s.end())
            ret = false;

        return ret;
    }
};