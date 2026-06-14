#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool is_mapped[256];
    char mapping[256];
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size())
            return false;

        for (int i=0; i<s.size(); i++) {
            int midx = s[i], tidx = t[i];
            if (mapping[midx] != t[i]) {
                if (is_mapped[tidx] || mapping[midx] != 0)
                    return false;
            }

            is_mapped[tidx] = true;
            mapping[midx] = t[i];
        }

        return true;
    }
};