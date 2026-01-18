#include <iostream>

using namespace std;

struct stack
{
    int data[10000];
    int top = -1;
};

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int n;
    cin >> n;
    stack st;

    // STL 사용
    for (int i = 0; i < n; i++)
    {
        string cmd;
        cin >> cmd;
        if (cmd == "push")
        {
            int param;
            cin >> param;
            st.data[++st.top] = param;
        }
        else if (cmd == "pop")
            cout << (st.top == -1 ? -1 : st.data[st.top--]) << '\n';
        else if (cmd == "size")
            cout << st.top + 1 << '\n';
        else if (cmd == "empty")
            cout << (st.top == -1 ? 1 : 0) << '\n';
        else
            cout << (st.top == -1 ? -1 : st.data[st.top]) << '\n';
    }
}
