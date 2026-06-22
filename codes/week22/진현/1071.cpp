#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1.size() > str2.size())
            swap(str1, str2);

        bool is_okay;
        string s;
        for (int i=0; i<str1.size(); i++) {
            s = str1.substr(0, str1.size() - i);

            is_okay = true;
            for (int j=0; j<str1.size(); j+=s.size()) {
                for (int k=0; k<s.size(); k++) {
                    if (str1[j + k] != s[k]) {
                        is_okay = false;
                        break;
                    }
                }

                if (!is_okay)
                    break;
            }
            for (int j=0; j<str2.size(); j+=s.size()) {
                for (int k=0; k<s.size(); k++) {
                    if (str2[j + k] != s[k]) {
                        is_okay = false;
                        break;
                    }
                }

                if (!is_okay)
                    break;
            }

            if (is_okay)
                break;
        }

        if (is_okay)
            return s;
        else
            return "";
    }
};