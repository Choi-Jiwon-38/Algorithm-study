#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> point;

#define MAX_N (6561)

string print_map[MAX_N];

void print_star(point p, int sz, char ch) {
    int &y = p.first, &x = p.second;
    if (sz == 1) {
        print_map[y] += ch;
    }
    else {
        int n_sz = sz / 3;

        print_star(p, n_sz, ch);
        print_star({y, x + n_sz}, n_sz, ch);
        print_star({y, x + n_sz + n_sz}, n_sz, ch);
        print_star({y + n_sz, x}, n_sz, ch);
        print_star({y + n_sz, x + n_sz}, n_sz, ' '); // center
        print_star({y + n_sz, x + n_sz + n_sz}, n_sz, ch);
        print_star({y + n_sz + n_sz, x}, n_sz, ch);
        print_star({y + n_sz + n_sz, x + n_sz}, n_sz, ch);
        print_star({y + n_sz + n_sz, x + n_sz + n_sz}, n_sz, ch);
    }
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N;
    cin >> N;
    print_star({0, 0}, N, '*');
    for (int i=0; i<N; i++)
        cout << print_map[i] << '\n';
}