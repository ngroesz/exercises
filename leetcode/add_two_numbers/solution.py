from typing import Optional
import pdb

# https://leetcode.com/problems/add-two-numbers/
# classification: medium

# list node code stolen from https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode

# Note: My initial misunderstanding of the problem led me to creating the reverseLinkedList function
# This function isn't really necessary. The result linked list could be created in the other direction
# and the function deleted.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
    return ListNode(arr[0], next=list_to_LL(arr[1:]))


class Solution:
    def reverseLinkedList(self, l: Optional[ListNode]):
      last = None

      while l.next:
        last = ListNode(l.val, next=last)
        l = l.next

      return ListNode(l.val, next=last)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        last = None

        remainder = 0
        while l1 or l2:
          l1_operand = l1.val if l1 else 0
          l2_operand = l2.val if l2 else 0
          result = l1_operand + l2_operand + remainder
          if result >= 10:
            remainder = 1
          else:
            remainder = 0
          last = ListNode(result % 10, next=last)

          if l1:
            l1 = l1.next
          if l2:
            l2 = l2.next

        if remainder:
            last = ListNode(remainder, next=last)

        return self.reverseLinkedList(last)

if __name__ == '__main__':
  s = Solution()

  print(
    s.addTwoNumbers(list_to_LL([2,4,3]), list_to_LL([5,6,4]))
  )
