"""
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_vals(node):
            value = []
            while (node):
                value.append(node.val)
                node = node.next
            return value

        l1 = get_vals(l1)
        l2 = get_vals(l2)

        l1.reverse()
        l2.reverse()

        l1 = int(''.join(map(str, l1)))
        l2 = int(''.join(map(str, l2)))

        l1 = [int(i) for i in str(l1 + l2)]
        l1.reverse()

        dummy = ListNode(0)
        crnt = dummy
        for val in l1:
            crnt.next = ListNode(val)
            crnt = crnt.next


        return dummy.next




""" Tests """
# Function to print a linked list for checking the results
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_addTwoNumbers():
    solution = Solution()

    # Test Case 1: 342 + 465 = 708
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = solution.addTwoNumbers(l1, l2)
    assert print_linked_list(result) == [7, 0, 8]

    # Test Case 2: 123 + 123 = 246
    l1 = ListNode(1, ListNode(2, ListNode(3)))
    l2 = ListNode(1, ListNode(2, ListNode(3)))
    result = solution.addTwoNumbers(l1, l2)
    assert print_linked_list(result) == [2, 4, 6]

    # Test Case 3: 9 + 1 = 10
    l1 = ListNode(9)
    l2 = ListNode(1)
    result = solution.addTwoNumbers(l1, l2)
    assert print_linked_list(result) == [0, 1]

    # Test Case 4: 0 + 0 = 0
    l1 = ListNode(0)
    l2 = ListNode(0)
    result = solution.addTwoNumbers(l1, l2)
    assert print_linked_list(result) == [0]

    print("All test cases passed.")

test_addTwoNumbers()