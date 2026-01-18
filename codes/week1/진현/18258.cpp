#include <bits/stdc++.h>

using namespace std;

struct _queue {
    int size;
    int *list;
    int f_idx;
    int b_idx;
};

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    struct _queue q;
    q.size = 0;
    q.f_idx = 0; q.b_idx = -1;
    q.list = new int[2000000];

    int t; cin >> t;
    while (t--) {
        string cmd; 
        cin >> cmd;

        switch (cmd[1])
        {
        case 'u': // push
            int x; cin >> x;
            q.size++;
            q.b_idx++;
            q.list[q.b_idx] = x;
            break;
        case 'o': // pop
            if (q.size) {
                q.size--;
                cout << q.list[q.f_idx] << '\n';
                q.f_idx++;
            }
            else {
                cout << -1 << '\n';
            }
            break;
        case 'i': // size
            cout << q.size << '\n';
            break;
        case 'm': // empty
            cout << (q.size == 0) << '\n';
            break;
        case 'r': // front
            if (q.size)
                cout << q.list[q.f_idx] << '\n';
            else
                cout << -1 << '\n';
            break;
        case 'a': // back
            if (q.size)
                cout << q.list[q.b_idx] << '\n';
            else
                cout << -1 << '\n';
            break;
        default:
            break;
        }
    }

    delete[] q.list;
    return 0;
}