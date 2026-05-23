#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int fibo[38];
    int tribonacci(int n) {
        fibo[0] = 0;
        fibo[1] = 1;
        fibo[2] = 1;
        for (int i=3; i<=37; i++)
            fibo[i] = fibo[i-1] + fibo[i-2] + fibo[i-3];
        
        return fibo[n];
    }
};