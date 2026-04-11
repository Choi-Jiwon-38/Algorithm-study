#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N;
    double ans = 0;
    vector<double> drinks;

    cin >> N;
    for (int i=0; i<N; i++) {
        double c;
        cin >> c;
        drinks.push_back(c);
    }

    sort(drinks.begin(), drinks.end());

    for (int i=0; i<N-1; i++)
        ans += (drinks[i] / 2);
    
    cout << drinks[N - 1] + ans;
}