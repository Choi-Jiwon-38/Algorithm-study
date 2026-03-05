#include <bits/stdc++.h>

using namespace std;

int visitors[250000];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, X, max_s, sum = 0, cnt = 1;
    cin >> N >> X;
    for (int i=0; i<N; i++)
        cin >> visitors[i];
    for (int i=0; i<X; i++)
        sum += visitors[i];
    max_s = sum;
    
    for (int e=X; e<N; e++) {
        sum += visitors[e];
        sum -= visitors[e - X];

        if (sum > max_s) {
            max_s = sum;
            cnt = 1;
        }
        else if (sum == max_s) {
            cnt++;
        }
    }

    if (max_s == 0) {
        cout << "SAD";
    }
    else {
        cout << max_s << '\n';
        cout << cnt;
    }
}