#include <bits/stdc++.h>

using namespace std;

#define height(x) (x.first)
#define rec_tower(x) (x.second)

// <height, rec_tower>
pair<int, int> tower[500001];

int main(void) {
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int t;
    cin >> t;
    for (int i=1; i<=t; i++) {
        int h, max_h_idx = 0;
        cin >> h;

        /**
         *  linear search를 수행하되, 특정 조건인 경우 해당 타워가 지닌 idx로 점프
         *  1. 현재 h가 탐색중인 타워의 h보다 큰 경우,
         *  1-1. 탐색중인 타워의 레이저를 수신하는 탑이 없는 (= rec_tower가 0) 경우 더 탐색할 필요가 없으므로 종료.
         *  1-2. 수신하는 탑이 있는 경우, 현재 i와 j 사이의 탑을 탐색할 필요가 없으므로 점프.
         *  2. h가 탐색중인 타워의 h보다 작은 경우,
         *    해당 타워가 레이저를 수신하므로, 탐색 종료.
         */
        for (int j=i-1; j>0; j--) {
            if (h >= height(tower[j])) {
                if (!rec_tower(tower[j])) {
                    max_h_idx = 0;
                    break;
                }
                else {
                    j = rec_tower(tower[j]);
                    // index 값 유지를 위해 +1
                    j++;
                }
            }
            else {
                max_h_idx = j;
                break;
            }
        }
        
        tower[i] = make_pair(h, max_h_idx);
        cout << max_h_idx << ' ';
    }

    return 0;
}
