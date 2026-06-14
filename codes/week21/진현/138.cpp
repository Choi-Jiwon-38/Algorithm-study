#include <bits/stdc++.h>

using namespace std;


// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};


class Solution {
public:
    int n_idx = 1;
    int memo_list[1001];
    Node* ptr_list[1001];
    map<Node*, int> rev_map;

    Node* copy_node(Node* node) {
        Node* ret = new Node(node->val);
        ptr_list[n_idx] = ret;

        if (node->random)
            memo_list[n_idx] = rev_map[node->random];

        n_idx++;
        return ret;
    }

    Node *copyRandomList(Node *head) {
        if (!head)
            return head;
        
        Node* cur_node = head;
        while (cur_node != nullptr) {
            rev_map.emplace(cur_node, n_idx);
            cur_node = cur_node->next;
            n_idx++;
        }

        n_idx = 1;
        cur_node = head;
        while (cur_node != nullptr) {
            copy_node(cur_node);
            cur_node = cur_node->next;
        }

        n_idx = 1;
        cur_node = ptr_list[n_idx];
        while (cur_node != nullptr) {
            if (memo_list[n_idx])
                cur_node->random = ptr_list[memo_list[n_idx]];
            if (n_idx < 1000)
                cur_node->next = ptr_list[n_idx + 1];

            cur_node = cur_node->next;
            n_idx++;
        }

        return ptr_list[1];
    }
};