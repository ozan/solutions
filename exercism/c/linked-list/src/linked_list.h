#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <stdbool.h>

#define ll_data_t int

struct list_item {
  ll_data_t data;
  struct list_item *next;
  struct list_item *prev;
};

struct list_item **new_list();
void delete_list(struct list_item **);
bool is_list_empty(struct list_item **);
bool push(struct list_item **, ll_data_t);
ll_data_t pop(struct list_item **);
bool unshift(struct list_item **, ll_data_t);
ll_data_t shift(struct list_item **);

#endif
