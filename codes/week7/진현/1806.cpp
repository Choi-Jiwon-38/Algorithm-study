#include <bits/stdc++.h>

using namespace std;

int nums[100000];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    int N, S, cnt, st, ed, sum = 0;
    cin >> N >> S;
    for (int i=0; i<N; i++)
        cin >> nums[i];
    for (int i=0; i<N; i++) {
        // ed 늘리기
        sum += nums[i];
        if (sum >= S) {
            st = 0;
            ed = i;
            cnt = i + 1;
            // st 줄이기
            while (sum >= S && st < ed) {
                if (sum - nums[st] < S) {
                    cnt = ed - st + 1;
                    break;
                }
                sum -= nums[st];
                st++;
            }
            break;
        }
    }
    // corner cases
    if (sum < S) {
        cout << 0;
        return 0;
    }
    else if (nums[N - 1] >= S) {
        cout << 1;
        return 0;
    }

    // N 사이즈 무빙
    while (ed < N - 1 && st < ed) {
        sum -= nums[st];
        sum += nums[ed + 1];

        // st 줄이기
        while (sum >= S && st < ed) {
            if (sum - nums[st + 1] < S) {
                cnt = ed - st + 1;
                break;
            }
            st++;
            sum -= nums[st];
        }

        st++;
        ed++;
    }
    cout << cnt;
}