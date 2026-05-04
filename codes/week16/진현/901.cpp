#include <bits/stdc++.h>

using namespace std;

class StockSpanner {
    vector<int> memo;
    int span_point, prev_span;
public:
    StockSpanner() {
        memo = vector<int>();
        span_point = 0;
        prev_span = 0;
    }
    
    int next(int price) {
        if (memo.size() >= 1 && price >= memo.back()) {
            prev_span++;
            for (; span_point>=0; span_point--) {
                if (price >= memo[span_point])
                    prev_span++;
                else
                    break;
            }
        }
        else {
            prev_span = 1;
            span_point = memo.size() - 1;
        }

        memo.push_back(price);
        return prev_span;
    }
};