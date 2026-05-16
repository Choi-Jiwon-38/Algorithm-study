#include <bits/stdc++.h>

using namespace std;

class Solution {
    bool b_bank[10];
    unordered_set<string> s_bank;
    queue<string> q1, q2;

public:
    void make_bank(vector<string>& bank) {
        for (auto s: bank)
            s_bank.insert(s);
    }

    void swap_queue() {
        q1 = q2;
        q2 = queue<string>();
    }

    int get_dist(string& s1, string& s2) {
        int dist = 0;
        for (int i=0; i<s1.size(); i++) {
            if (s1[i] != s2[i])
                dist++;
        }
        return dist;
    }

    int minMutation(string startGene, string endGene, vector<string>& bank) {
        int step = 0;
        make_bank(bank);

        if (startGene == endGene)
            return step;
        else if (s_bank.find(endGene) == s_bank.end())
            return -1;

        q1.push(startGene);
        while (!q1.empty()) {
            while (q1.size()) {
                string tg = q1.front();
                q1.pop();

                for (int i=0; i<bank.size(); i++) {
                    string& b_s = bank[i];
                    if (b_bank[i])
                        continue;

                    if (get_dist(b_s, tg) == 1) {
                        b_bank[i] = true;
                        if (get_dist(b_s, endGene) <= 1)
                            return step + get_dist(b_s, endGene) + 1;
                        else
                            q2.push(b_s);
                    }
                }
            }

            step++;
            swap_queue();
        }

        return -1;
    }
};