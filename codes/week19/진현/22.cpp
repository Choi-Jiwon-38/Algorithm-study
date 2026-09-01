#include <bits/stdc++.h>

using namespace std;

class Solution {
    int sz;
    vector<string> v;
public:
    void make_strs(string s) {
        if (s.size() == sz) {
            v.push_back(s);
            return;
        }

        make_strs(s + '(');
        make_strs(s + ')');
    }

    bool check_parentheses(string& s) {
        int t = 0;
        for (auto it=s.rbegin(); it!=s.rend(); it++) {
            if (*it == ')')
                t++;
            else
                t--;

            if (t < 0)
                break;
        }
        return (t == 0);
    }

    vector<string> generateParenthesis(int n) {
        vector<string> ret;

        sz = n * 2;
        make_strs("");

        for (auto s: v) {
            if (check_parentheses(s))
                ret.push_back(s);
        }
        return ret;
    }
};