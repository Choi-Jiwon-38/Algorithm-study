#include <bits/stdc++.h>

using namespace std;

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int mid, l = 1, r = n;

        while (1) {
            mid = l + (r - l) / 2;

            int ret = guess(mid);
            if (ret == -1)
                r = mid - 1;
            else if (ret == 1)
                l = mid + 1;
            else
                break;
        }
        return mid;
    }
};