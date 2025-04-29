#234. Palindrome Linked List
"""
Given the head of a singly linked list, return true if
 it is a palindrome or false otherwise.

Example
Input: head = [1,2,2,1]
Output: true

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
"""

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast:
            slow = slow.next

        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        return True