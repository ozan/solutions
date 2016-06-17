struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
  int maxDepth(TreeNode *root) {
    if (root == nullptr)
      return 0;
    int leftMax = maxDepth(root->left);
    int rightMax = maxDepth(root->right);
    return 1 + (leftMax > rightMax ? leftMax : rightMax);
  }
};
