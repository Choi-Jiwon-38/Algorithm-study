#include <bits/stdc++.h>

using namespace std;

 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* cur = head, *c_head = new ListNode, *c_cur = c_head;
        
        while (cur != nullptr) {
            bool is_distinct = true;
            int cur_val = cur->val;

            while (cur->next) {
                if (cur->next->val == cur_val) {
                    is_distinct = false;
                    cur = cur->next;
                }
                else {
                    break;
                }
            }

            if (is_distinct) {
                c_cur->next = new ListNode;
                c_cur = c_cur->next;
                c_cur->val = cur->val;
            }
            cur = cur->next;
        }

        return c_head->next;
    }
};