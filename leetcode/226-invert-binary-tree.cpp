class Solution {
public:
  TreeNode *invertTree(TreeNode *root) {
    if (root == nullptr)
      return nullptr;
    TreeNode *tmp = invertTree(root->left);
    root->left = invertTree(root->right);
    root->right = tmp;
    return root;
  }
};
