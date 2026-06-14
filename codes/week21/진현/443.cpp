#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        int sz = chars.size(), tg = 0;

        char prev = chars[0];
        int cnt = 1;
        for (int i=1; i<sz; i++) {
            if (chars[i] != prev) {
                chars[tg++] = prev;

                if (cnt > 1) {
                    string s = to_string(cnt);
                    for (auto ch: s) 
                        chars[tg++] = ch;
                }

                prev = chars[i];
                cnt = 1;
            }
            else {
                cnt++;
            }
        }

        chars[tg++] = prev;
        if (cnt > 1){
            string s = to_string(cnt);
            for (auto ch : s)
                chars[tg++] = ch;
        }

        return tg;
    }
};