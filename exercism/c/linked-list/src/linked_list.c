#include "linked_list.h"
#include <stdlib.h>

/*
 * A circular doubly linked list with O(1) push, pop, shift and unshift.
 *
 * The `prev` of the "first" node is by convention the tail of the list.
 */

// Allocate an empty list, which is simply a pointer to a null `list_item`
struct list_item **new_list() {
  struct list_item **item = malloc(sizeof(struct list_item *));
  *item = NULL;
  return item;
}

// A list is empty if it points to a null `list_item`
bool is_list_empty(struct list_item **l) { return l == NULL || *l == NULL; }

// Add a new node to the tail of the list
bool push(struct list_item **list, ll_data_t data) {
  if (list == NULL)
    return false;

  // construct the node
  struct list_item **item = new_list();
  *item = malloc(sizeof(struct list_item));
  (*item)->data = data;

  if (is_list_empty(list)) {
    // if empty, treat the new node as the entire list
    (*item)->next = (*item)->prev = *item;
    *list = *item;
  } else {
    // if list is not empty, update all 4 pointers required to insert new node
    (*item)->prev = (*list)->prev;
    (*item)->next = *list;
    (*list)->prev->next = *item;
    (*list)->prev = *item;
  }
  return true;
}

// Add a node at the tail then rotate by one place, to have added at "head"
bool unshift(struct list_item **list, ll_data_t data) {
  bool result = push(list, data);
  if (result)
    *list = (*list)->prev;
  return result;
}


// Remove and return the tail of the list
ll_data_t pop(struct list_item **list) {
  struct list_item *tail = (*list)->prev;
  ll_data_t data = tail->data;

  if (*list == tail) {
    *list = NULL;
  } else {
    tail->prev->next = tail->next;
    tail->next->prev = tail->prev;
  }

  free(tail);
  return data;
}

// Remove and return the head of the list
ll_data_t shift(struct list_item **list) {
  *list = (*list)->next;
  return pop(list);
}

// To delete a list, we free all of its items
void delete_list(struct list_item **list) {
  while (!is_list_empty(list))
    pop(list);
}

