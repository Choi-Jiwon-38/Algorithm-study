#include <bits/stdc++.h>

using namespace std;

class Solution {
    int cnt[26];
public:
    inline int get_vowels() {
        return (cnt[0] + cnt['e' - 'a'] + cnt['i' - 'a'] + cnt['o' - 'a'] + cnt['u' - 'a']);
    }

    int maxVowels(string s, int k) {
        for (int i=0; i<k; i++)
            cnt[s[i] - 'a']++;
        int ret = get_vowels();
        
        for (int i=k; i<s.size(); i++) {
            int l = i - k, r = i;

            cnt[s[l] - 'a']--;
            cnt[s[r] - 'a']++;
            ret = max(ret, get_vowels());
        }

        return ret;
    }
};