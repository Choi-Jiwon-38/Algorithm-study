#include <bits/stdc++.h>

using namespace std;

int N;

bool check(string& str) {
    bool is_okay = true;
    int i_e_idx = str.size() - 1;
    int sz = (str.size() / 2) + 1;

    for (int s=0; s<sz; s++) {
        int e_idx = i_e_idx - s, s_idx = (e_idx - 1) - s;

        if (s_idx < 0)
            break;

        while (e_idx < str.size()) {
            if (str[s_idx] != str[e_idx])
                break;
            
            s_idx++;
            e_idx++;
        }
        if (e_idx == str.size()) {
            is_okay = false;
            break;
        }
    }

    return is_okay;
}

void dfs(string& str) {
    if (str.size() == N) {
        cout << str;
        exit(0);
    }

    for (char i='1'; i<='3'; i++) {
        str += i;
        if (check(str))
            dfs(str);
        str.pop_back();
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    cin >> N;

    string s = "";
    dfs(s);
    return 0;
}