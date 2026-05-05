#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> point;

string video[64];

bool is_uniform(point p, int sz) {
    bool ret = true;
    int &y = p.first, &x = p.second;
    char& cmp = video[y][x];
    for (int i=y; i<y+sz; i++) {
        for (int j=x; j<x+sz; j++) {
            if (cmp != video[i][j]) {
                ret = false;
                break;
            }
        }

        if (!ret)
            break;
    }
    return ret;
}

void quad_tree(string& s, point p, int sz) {
    int &y = p.first, &x = p.second;
    if (sz <= 1) {
        s += video[y][x];
        return;
    }
    else {
        string t_s[4];
        int n_sz = sz >> 1, ny = y + n_sz, nx = x + n_sz;

        quad_tree(t_s[0], p, n_sz);
        quad_tree(t_s[1], {y, nx}, n_sz);
        quad_tree(t_s[2], {ny, x}, n_sz);
        quad_tree(t_s[3], {ny, nx}, n_sz);

        if (!is_uniform(p, sz)) {
            s += ('(' + t_s[0] + t_s[1] + t_s[2] + t_s[3] + ')');
        }
        else {
            s += t_s[0];
        }
        
        return;
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N;
    cin >> N;
    for (int i=0; i<N; i++)
        cin >> video[i];

    string ans = "";
    quad_tree(ans, {0, 0}, N);
    cout << ans;
    return 0;
}