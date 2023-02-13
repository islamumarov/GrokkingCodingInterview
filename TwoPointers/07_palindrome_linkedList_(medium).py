from node import Node


class palindrome_linkedlist:
    def is_palindromic_linkedlist(self, head: Node):
        if head is None or head.next is None:
            return True
        mid = self.get_middle(head)
        reversed_half_head = self.reverse_half(mid)
        while head is not None and reversed_half_head is not None:
            if head.data != reversed_half_head.data:
                return False
            head = head.next
            reversed_half_head = reversed_half_head.next
        return True

    def reverse_half(self, head: Node):
        prev = None
        current = head
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev

    def get_middle(self, head: Node):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    solution = palindrome_linkedlist()

    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    solution.is_palindromic_linkedlist(head)


