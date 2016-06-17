
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
  ListNode *reverseList(ListNode *head) {
    if (!head || !(head->next))
      return head;
    ListNode *node = reverseList(head->next);
    head->next->next = head;
    head->next = nullptr;
    return node;
  }
};
