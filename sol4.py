#!/usr/bin/python
# You are given two linked lists representing two non-negative numbers. The
# digits are stored in reverse order and each of their nodes contain a single
# digit. Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None
    
class Solution:
  # @signature(int, str, int)
  # @return a ListNode
  def addTwoNumbers(self, l1, l2):
    l1 = l1
    l2 = l2
    t3 = ListNode(0)
    l3 = t3

    carry = 0
    while(l1 != None and l2 != None):
      t3.next = ListNode((carry + l1.val + l2.val)%10)
      carry = (carry + l1.val + l2.val)/10
      l1 = l1.next
      l2 = l2.next
      t3 = t3.next
 
    if(None == l1 and None != l2):
      while(l2 != None):
        t3.next = ListNode((carry + l2.val)%10)
        carry = (carry + l2.val)/10
        l2 = l2.next
        t3 = t3.next
        
    if(None == l2 and None != l1):
      while(l1 != None):
        t3.next = ListNode((carry + l1.val)%10)
        carry = (carry + l1.val)/10
        l1 = l1.next
        t3 = t3.next

    if(0 != carry):
      t3.next = ListNode(carry)

    return l3.next
    
if __name__ == '__main__':
  n1 = ListNode(5)
  n2 = ListNode(4)
  n3 = ListNode(3)
#  n1.next = n2
#  n2.next = n3

  m1 = ListNode(5)
  m2 = ListNode(6)
  m3 = ListNode(4)
#  m1.next = m2
#  m2.next = m3

  s = Solution()
  n1 = s.addTwoNumbers(n1, m1)
  while(None != n1):
    print "Hi " + str(n1.val)
    n1 = n1.next
