#include <bits/stdc++.h>

using namespace std;

#define get_name(x) (x.first)
#define get_count(x) (x.second)


struct _trie_node {
    int count; // Terminal Node인 경우에만 사용.
    bool is_terminal;
    _trie_node *child[96]; // From ASCII...
};

struct _trie {
    int size;
    _trie_node *root;
};

_trie trie;

inline void init_node(_trie_node **ptr) {
    if (!(*ptr)) {
        _trie_node *p = new _trie_node;
        p->count = 0;
        p->is_terminal = false;
        memset(p->child, 0, sizeof(p->child));

        *ptr = p;
    }
}

void insert(string str) {
    _trie_node *cur_node = trie.root;

    for (char ch: str) {
        int ascii;
        ascii = (ch - ' ');
        if (0 <= ascii && ascii < 96) {
            init_node(&(cur_node->child[ascii]));
            cur_node = cur_node->child[ascii];
        }
    }

    trie.size++;
    cur_node->count++;
    cur_node->is_terminal = true;
}

void dfs(vector<pair<string, int>>& v, _trie_node *n, string s) {
    if (n->is_terminal) {
        v.push_back(make_pair(s, n->count));
    }

    for (int i=0; i<96; i++) {
        // child[i] != nullptr
        if (n->child[i]) {
            string tmp_s = s;
            tmp_s = s + (char)(' ' + i);

            dfs(v, n->child[i], tmp_s);
        }
    }
}

void print_trie(void) {
    vector<pair<string, int>> v;
    dfs(v, trie.root, string());

    for (auto ea: v)
        cout << get_name(ea) << ' ' << ((float)get_count(ea) / trie.size * 100) << '\n';
}

int main(void) {
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    cout << fixed;
    cout.precision(4);
    init_node(&(trie.root));

    string inp;
    while (getline(cin, inp)) {
        if (inp == "")
            break;
        
        insert(inp);
    }

    print_trie();
    return 0;
}