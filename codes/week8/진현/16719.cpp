#include <bits/stdc++.h>

using namespace std;

string char_to_str(deque<char>& str) {
    string s = "";
    for (char ch: str)
        s += ch;
    return s;
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    deque<char> deq;
    string s;
    vector<string> v;

    cin >> s;
    v.push_back(s);
    for (char ch: s)
        deq.push_back(ch);

    for (int l=deq.size(); l>1; l--) {
        string s;
        auto iter = deq.begin();

        for (int i=0; i<deq.size() - 1; i++, iter++) {
            if (deq[i] > deq[i + 1])
                break;
        }

        deq.erase(iter);
        s = char_to_str(deq);
        v.push_back(s);
    }

    for (auto iter=v.rbegin(); iter!=v.rend(); iter++)
        cout << *iter << '\n';
}