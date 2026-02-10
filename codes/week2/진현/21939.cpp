#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

struct cmp_hard {
    bool operator()(pii &a, pii &b) {
        if (a.second == b.second)
            return a.first < b.first;
        else
            return a.second < b.second;
    }
};

struct cmp_easy {
    bool operator()(pii &a, pii &b) {
        if (a.second == b.second)
            return a.first > b.first;
        else
            return a.second > b.second;
    }
};

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    map<int, int> problem_map;
    priority_queue<pii, vector<pii>, cmp_hard> hard_list;
    priority_queue<pii, vector<pii>, cmp_easy> easy_list;
    
    int N, M;
    cin >> N;
    while (N--) {
        int P, L;
        cin >> P >> L;
        pii tp = make_pair(P, L);

        problem_map.insert(tp);
        hard_list.push(tp);
        easy_list.push(tp);
    }

    cin >> M;
    while (M--) {
        int P, L;
        string cmd;
        cin >> cmd >> P;
        switch (cmd[0]) {
            case 'r': { // recommend 
                pii tg = (P == 1 ? hard_list.top() : easy_list.top());
                while (problem_map.find(tg.first)->second != tg.second) {
                    if (P == 1)
                        hard_list.pop();
                    else
                        easy_list.pop();
                    tg = (P == 1 ? hard_list.top() : easy_list.top());
                }
                cout << tg.first << '\n';
                break;
            }
            case 'a': { // add
                cin >> L;
                pii tp = make_pair(P, L);
                auto iter = problem_map.find(P);

                if (iter != problem_map.end()) {
                    iter->second = L;
                    hard_list.push(tp);
                    easy_list.push(tp);
                }
                else {
                    problem_map.insert(tp);
                    hard_list.push(tp);
                    easy_list.push(tp);
                }
                break;
            }
            case 's': { // solved
                problem_map.find(P)->second = 0;
                break;
            }
            default:
                break;
        }
    }
}