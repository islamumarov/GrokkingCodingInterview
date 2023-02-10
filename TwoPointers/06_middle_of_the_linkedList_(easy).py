from node import Node


class middle_of_linkedlist:
    def find_middle(self, head: Node):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow



if __name__ == '__main__':
