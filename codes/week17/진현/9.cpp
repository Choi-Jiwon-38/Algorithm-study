#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string s = to_string(x);

        int ed_idx = s.size() - 1;
        for (int i=0; i<s.size()/2; i++) {
            if (s[i] != s[ed_idx - i])
                return false;
        }
        return true;
    }
};