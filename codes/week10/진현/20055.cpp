#include <bits/stdc++.h>

using namespace std;

struct node {
    int id;
    int durab;
    bool is_robot;
    node* next;

    void init(int _id, int d, node* p) {
        id = _id;
        durab = d;
        is_robot = false;
        next = p;
    }
} b_node[201];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, K, T_N;
    deque<node*> belt, r_belt;
    cin >> N >> K;
    T_N = 2 * N;
    for (int i=1; i<=T_N; i++) {
        int d;
        cin >> d;

        b_node[i].init(i, d, &b_node[i % T_N + 1]);

        if (i <= N)
            belt.push_back(&b_node[i]);
        else
            r_belt.push_front(&b_node[i]);
    }

    int step = 1;
    for (;;step++) {
        // 1-1. upside
        belt.push_front(r_belt.front());
        r_belt.pop_front();
        // 1-2. downside
        r_belt.push_back(belt.back());
        belt.pop_back();
        // 1-3. check N
        if (belt.back()->is_robot)
            belt.back()->is_robot = false;

        // 2.
        for (auto it = belt.rbegin() + 1; it!=belt.rend(); it++) {
            node* cur_node = *it, *next_node = cur_node->next;
            if (cur_node->is_robot && next_node->durab >= 1 && !next_node->is_robot) {
                cur_node->is_robot = false;

                next_node->durab--;
                if (next_node != belt.back()) {
                    next_node->is_robot = true;
                }
            }
        }

        // 3.
        if (belt.front()->durab >= 1 && !belt.front()->is_robot) {
            belt.front()->is_robot = true;
            belt.front()->durab--;
        }

        // 4.
        int z_cnt = 0;
        for (int i=1; i<=T_N; i++) {
            if (b_node[i].durab == 0)
                z_cnt++;
        }

        if (z_cnt >= K)
            break;
    }

    cout << step;
}