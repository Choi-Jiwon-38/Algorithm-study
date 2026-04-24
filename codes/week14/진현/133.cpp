#include <bits/stdc++.h>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

bool is_copied[101];
Node graph[101];

class Solution {
public:
    void init() {
        for (int i=1; i<=100; i++) {
            graph[i] = Node();
            is_copied[i] = false;
        }
    }

    bool copy_node(Node* node) {
        if (node) {
            vector<Node*> neighbors;
            for (auto nb: node->neighbors) {
                Node* copied_nb = &graph[nb->val];
                neighbors.push_back(copied_nb);
            }

            graph[node->val] = Node(node->val, neighbors);

            return true;
        }

        // empty graph
        else {
            return false;
        }
    }

    void enqueue_node(Node* node, queue<Node*>& q) {
        if (node) {
            for (auto nb: node->neighbors) {
                if (!is_copied[nb->val]) {
                    q.push(nb);
                    is_copied[nb->val] = true;
                }
            }
        }
    }

    Node* cloneGraph(Node* _node) {
        init();

        is_copied[1] = true;
        if (!copy_node(_node))
            return nullptr;

        queue<Node*> q;
        enqueue_node(_node, q);
        while (q.size()) {
            auto node = q.front();
            q.pop();

            copy_node(node);
            enqueue_node(node, q);
        }

        return &graph[1];
    }
};