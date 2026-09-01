#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> v;
        map<vector<int>, vector<string>> m;

        for (auto str: strs) {
            vector<int> cnt;
            
            cnt.assign(26, 0);
            for (auto ch: str)
                cnt[ch - '0']++;

            if (m.find(cnt) == m.end())
                m[cnt] = vector<string>();
            m[cnt].push_back(str);
        }

        for (auto [h, t_v]: m)
            v.push_back(t_v);
        return v;
    }
};