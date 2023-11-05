from GrokkingCodingInterview.TwoPointers.node import Node
# https://leetcode.com/problems/reorder-list/description/


if __name__ == '__main__':
    solution = rearrange_linkedlist()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    reordered_head = solution.reorder(head)
    while reordered_head is not None:
        print(" ---> ", reordered_head.data, " --->  ")
        reordered_head = reordered_head.next

