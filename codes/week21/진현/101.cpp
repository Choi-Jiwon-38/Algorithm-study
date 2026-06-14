#include <bits/stdc++.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    void build_tree(vector<int>& v, TreeNode* node, bool rev) {
        if (node == nullptr) {
            v.push_back(-101);
            return;
        }
        v.push_back(node->val);

        if (rev) {
            build_tree(v, node->left, rev);
            build_tree(v, node->right, rev);
        }
        else {
            build_tree(v, node->right, rev);
            build_tree(v, node->left, rev);
        }
    }

    bool isSymmetric(TreeNode* root) {
        vector<int> lv, rv;

        if (!root) 
            return true;
        
        build_tree(lv, root->left, true);
        build_tree(rv, root->right, false);

        if (lv.size() != rv.size())
            return false;

        for (int i=0; i<lv.size(); i++) {
            if (lv[i] != rv[i])
                return false;
        }

        return true;
    }
};