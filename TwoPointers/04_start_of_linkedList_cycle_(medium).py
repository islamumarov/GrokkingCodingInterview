class start_of_linkedlist_cycle:
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None

    def find_first_node(self, head, cycle_len):
        slow = fast = head
        while cycle_len > 0:
            fast = fast.next
            cycle_len -= 1
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def cycle_len(self, head):
        slow = fast = head
        cycle_len = 0
        while True:
            fast = fast.next
            cycle_len += 1
            if fast == slow:
                break
        return cycle_len

    def find_cycle_start(self, head):
        slow = head
        fast = head
        cycle_len = 0
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycle_len = self.cycle_len(slow)
                break
        return self.find_first_node(head, cycle_len)


if __name__ == '__main__':
    solution = start_of_linkedlist_cycle()
    head = solution.Node(1)
    head.next = solution.Node(2)
    head.next.next = solution.Node(3)
    head.next.next.next = solution.Node(4)
    head.next.next.next.next = solution.Node(5)
    head.next.next.next.next.next = solution.Node(6)
    head.next.next.next.next.next.next = solution.Node(7)
    head.next.next.next.next.next.next.next = head.next.next

    cycle_node = solution.find_cycle_start(head)
    print("first cycle node = ", cycle_node.data)