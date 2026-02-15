#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> pii;

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N;
    vector<pii> lectures;
    priority_queue<int, vector<int>, greater<int>> pq;
    cin >> N;

    for (int i=0; i<N; i++) {
        int a, b;
        cin >> a >> b;
        lectures.push_back(make_pair(a, b));
    }

    sort(lectures.begin(), lectures.end());

    pq.push(lectures[0].second);
    for (int i=1; i<N; i++) {
        int s_i = lectures[i].first, t_i = lectures[i].second;

        if (s_i < pq.top()) {
            pq.push(t_i);
        }
        else {
            pq.pop();
            pq.push(t_i);
        }
    }

    cout << pq.size();
}