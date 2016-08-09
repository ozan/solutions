#include <vector>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
  int rob(TreeNode *root) {
    auto res = rob_node(root);
    // pair representing skip, take
    return max(res.first, res.second);
  }

  pair<int, int> rob_node(TreeNode *node) {
    pair<int, int> res;
    if (node == nullptr)
      return res;

    auto left = rob_node(node->left);
    auto right = rob_node(node->right);

    res.first = max(left.first, left.second) + max(right.first, right.second);
    res.second = node->val + left.first + right.first;
    return res;
  }
};
