#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int tg = 0, idx = 0;
        while (tg < s.size() && idx < t.size()) {
            while (idx < s.size() && s[tg] != t[idx])
                idx++;
            
            if (idx < s.size()) {
                tg++;
                idx++;
            }
            else {
                break;
            }
        }
            
        return tg == s.size();
    }
};