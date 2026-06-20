class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if there are at least k nodes left
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next

        # Reverse current k group
        new_head = self.reverse(head, k)

        # Recurse for the remaining list and connect it
        head.next = self.reverseKGroup(curr, k)

        return new_head

    def reverse(self, head, k):
        count = 0
        prev, curr = None, head

        while count < k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1

        return prev