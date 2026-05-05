#include <bits/stdc++.h>

using namespace std;

vector<int> mat_1[1024], mat_2[1024];
bool clear_1 = true;

void clear_mat(int N) {
    for (int i=0; i<N; i++) {
        if (clear_1)
            mat_1[i].clear();
        else
            mat_2[i].clear();
    }
    clear_1 = !clear_1;
}

int polling(int i, int j) {
    int temp[4];
    if (clear_1) {
        temp[0] = mat_1[i][j]; temp[1] = mat_1[i][j+1];
        temp[2] = mat_1[i+1][j]; temp[3] = mat_1[i+1][j+1];
    }
    else {
        temp[0] = mat_2[i][j]; temp[1] = mat_2[i][j+1];
        temp[2] = mat_2[i+1][j]; temp[3] = mat_2[i+1][j+1];
    }
    sort(begin(temp), begin(temp) + 4);
    return temp[2];
}

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);
    
    int _N;
    cin >> _N;
    for (int i=0; i<_N; i++) {
        for (int j=0; j<_N; j++) {
            int c;
            cin >> c;
            mat_1[i].push_back(c);
        }
    }

    for (int N=_N; N>1; N>>=1) {
        for (int i=0; i<N; i+=2) {
            vector<int>& mat = (clear_1 ? mat_2[i / 2] : mat_1[i / 2]);
            for (int j=0; j<N; j+=2)
                mat.push_back(polling(i, j));
        }
        clear_mat(N >> 1);
    }
    cout << (clear_1 ? mat_1[0][0] : mat_2[0][0]);
}   