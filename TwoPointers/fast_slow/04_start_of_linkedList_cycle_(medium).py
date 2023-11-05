
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
