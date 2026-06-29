#include <bits/stdc++.h>

using namespace std;

class WordDictionary {
public:
    set<string> dict;

    WordDictionary() {
        dict = set<string>();
    }
    
    void addWord(string word) {
        dict.insert(word);
    }
    
    bool search(string word) {
        auto it = dict.lower_bound(word);
        return it != dict.end();
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */