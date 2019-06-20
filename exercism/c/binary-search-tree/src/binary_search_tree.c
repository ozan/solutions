#include "binary_search_tree.h"
#include <stdlib.h>

// Construct a node with given data
node_t *create_node(int data) {
  node_t *node = malloc(sizeof(node_t));
  node->data = data;
  node->left = NULL;
  node->right = NULL;
  return node;
}

// Recursively traverse tree, insert node in correct location
void add_node(node_t **tree, node_t *node) {
  if (*tree == NULL) {
    *tree = node;
    return;
  }
  if (node->data <= (*tree)->data)
    add_node(&((*tree)->left), node);
  else
    add_node(&((*tree)->right), node);
}

// Iteratively construct tree from data by adding each node
node_t *build_tree(int tree_data[], int size) {
  node_t *tree = NULL;
  for (int i = 0; i < size; i++)
    add_node(&tree, create_node(tree_data[i]));
  return tree;
}

// Recursively count nodes in tree
int count_nodes(node_t *tree) {
  if (tree == NULL)
    return 0;
  return 1 + count_nodes(tree->left) + count_nodes(tree->right);
}

// Recursively fill array with the in-order DFS traversal of the tree
int inorder_fill(int *target, node_t *tree, int i) {
  if (tree == NULL)
    return i;
  i = inorder_fill(target, tree->left, i);
  target[i++] = tree->data;
  i = inorder_fill(target, tree->right, i);
  return i;
}

// Retrieve sort order of tree by in-order filling an array
int *sorted_data(node_t *tree) {
  int len = count_nodes(tree);
  int *sorted = malloc(len * sizeof(int));
  inorder_fill(sorted, tree, 0);
  return sorted;
}

// Recursively free entire tree
void free_tree(node_t *tree) {
  if (tree == NULL)
    return;
  free_tree(tree->left);
  free_tree(tree->right);
  free(tree);
}

