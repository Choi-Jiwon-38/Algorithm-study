#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    set<char> visible;
    map<string, map<string, double>> m;

    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        vector<double> ans;

        for (int i=0; i<equations.size(); i++) {
            string& divisor = equations[i][0], diviend = equations[i][1];
            for (auto ch: divisor)
                visible.insert(ch);
            for (auto ch: diviend)
                visible.insert(ch);

            m[divisor].emplace(diviend, values[i]);
            m[diviend].emplace(divisor, 1 / values[i]);
        }

        for (auto query: queries) {
            bool is_found = false;
            string& divisor = query[0], diviend = query[1];
            for (auto ch: divisor) {
                if (visible.find(ch) == visible.end()) {
                    is_found = true;
                    ans.push_back(-1.0);
                    break;
                }
            }
            if (is_found)
                continue;
            
            for (auto ch: diviend) {
                if (visible.find(ch) == visible.end()) {
                    is_found = true;
                    ans.push_back(-1.0);
                    break;
                }
             }
            if (is_found)
                continue;
            
            set<string> visited;
            queue<pair<string, double>> q;
            q.push({divisor, 1.0});
            while (q.size()) {
                string tg = q.front().first;
                double val = q.front().second;
                q.pop();
                for (auto [k, v]: m[tg]) {
                    if (k == diviend) {
                        ans.push_back(val * v);
                        is_found = true;
                        break;
                    }
                    else if (visited.find(k) == visited.end()) {
                        q.emplace(k, val * v);
                        visited.insert(k);
                    }
                }

                if (is_found)
                    break;
            }

            if (!is_found)
                ans.push_back(-1.0);
        }

        return ans;
    }
};