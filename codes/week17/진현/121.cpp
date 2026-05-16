#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0, min_price = INT_MAX;
    
        for (int i=0; i<prices.size(); i++) {
            min_price = min(prices[i], min_price);

            if (prices[i] - min_price > profit)
                profit = prices[i] - min_price;
        }

        return profit;
    }
};
