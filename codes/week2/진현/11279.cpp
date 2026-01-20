#include <bits/stdc++.h>

using namespace std;

int main()
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int n, x;
    priority_queue<int> max_heap;

    cin >> n;
    while (n--)
    {
        cin >> x;
        switch (x)
        {
        case 0:
            if (max_heap.empty())
                cout << 0;
            else
            {
                cout << max_heap.top();
                max_heap.pop();
            }
            cout << '\n';
            break;

        default:
            max_heap.push(x);
            break;
        }
    }
    return 0;
}