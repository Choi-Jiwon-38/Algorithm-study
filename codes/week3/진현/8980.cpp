#include <bits/stdc++.h>

using namespace std;

typedef tuple<int, int, int> ti3;
#define at(x, k) (get<k>(x))

int carry_memo[2001], carry_box[2001];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    priority_queue<ti3, vector<ti3>, greater<ti3>> pq;
    int N, C, M, ans = 0;
    cin >> N >> C >> M;

    for (int i=0; i<M; i++) {
        int from, dest, nr_box;
        cin >> from >> dest >> nr_box;
        pq.push(make_tuple(dest, -nr_box, from)); 
    }

    while (!pq.empty()) {
        ti3 info = pq.top();
        pq.pop();
        int st = at(info, 2), end = at(info, 0), nr_box = -at(info, 1);

        // cout << "orig: " << st << ' ' << end << ' ' << nr_box << endl;

        // verify
        bool is_lt = true;
        for (int p=st; p<end; p++) {
            if (carry_memo[p] + nr_box > C) {
                if (carry_memo[p] == C) {
                    is_lt = false;
                    break;
                }
                else {
                    nr_box = C - carry_memo[p];
                }
            }  
        }
        if (!is_lt)
            continue;

        // carrying
        carry_box[st] += nr_box;
        for (int p=st; p<end; p++) {
            carry_memo[p] += nr_box;
        }

        // cout << "tg: " << st << ' ' << end << ' ' << nr_box << endl;
        // cout << "memo: ";
        // for (int i = 1; i <= N; i++)
        //     cout << carry_memo[i] << ' ';
        // cout << endl;
    }

    // cout << "box: ";
    // for (int i = 1; i <= N; i++)
    //     cout << carry_box[i] << ' ';
    // cout << endl;

    for (int i=0; i<N; i++)
        ans += carry_box[i];
    cout << ans;
}