class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        source = []

        while head is not None:
            source.append(head.val)
            head = head.next

        return source == source[::-1]