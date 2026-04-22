#include <bits/stdc++.h>

using namespace std;

int N;
int pre_list[1000], ino_list[1000];

void postorder(int r_idx, int ino_st, int ino_ed) {
    if (ino_st > ino_ed)
        return;

    int& root = pre_list[r_idx];
    
    int r_ino = ino_st;
    while (root != ino_list[r_ino])
        r_ino++;

    postorder(r_idx + 1, ino_st, r_ino - 1);
    postorder(r_idx + (r_ino - ino_st + 1), r_ino + 1, ino_ed);
    
    cout << root << ' ';
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int T;
    cin >> T;
    while (T--) {
        int root;
        cin >> N;
        for (int i=0; i<N; i++)
            cin >> pre_list[i];
        for (int i=0; i<N; i++)
            cin >> ino_list[i];

        postorder(0, 0, N - 1);
        cout << '\n';
    }
}