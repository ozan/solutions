
typedef struct node_t {
  int data;
  struct node_t *left;
  struct node_t *right;
} node_t;

node_t *build_tree(int tree_data[], int size);
void free_tree(node_t *tree);
int *sorted_data(node_t *tree);
