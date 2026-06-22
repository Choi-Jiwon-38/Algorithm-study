#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
    set<ListNode*> p_set;
public:
    bool hasCycle(ListNode *head) {
        if (!head)
            return false;

        auto cur = head->next;
        while (cur != nullptr) {
            if (p_set.find(cur) != p_set.end())
                return true;

            p_set.insert(cur);
            cur = cur->next;
        }

        return false;
    }
};