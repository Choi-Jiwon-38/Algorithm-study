#include <bits/stdc++.h>

using namespace std;

class Solution {
    int ws1[26], ws2[26];
public:
    bool closeStrings(string word1, string word2) {
        if (word1.length() != word2.length())
            return false;

        for (char ch: word1)
            ws1[ch - 'a']++;
        for (char ch: word2)
            ws2[ch - 'a']++;

        for (int i=0; i<26; i++) {
            if (ws1[i] == 0 && ws2[i] > 0)
                return false;
            if (ws1[i] > 0 && ws2[i] == 0)
                return false;
        }

        sort(begin(ws1), end(ws1));
        sort(begin(ws2), end(ws2));

        for (int i=26; i>=0; i++) {
            if (ws1[i] != ws2[i])
                return false;
            
            if (ws1[i] == 0 && ws2[i] == 0)
                break;
        }

        return true;
    }
};