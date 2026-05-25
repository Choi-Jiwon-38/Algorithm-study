#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {
        int idx = haystack.find(needle);
        return (idx == string().npos ? -1 : idx);
    }
};