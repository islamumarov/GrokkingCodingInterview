from typing import Optional

from TwoPointers.node import Node


class ReverseSubList:

    def reverse_sub(self, head: Optional[Node], left: int, right: int) -> Node:

        if left == right:
            return head

        curr, prev = head, None
        i = 0
        while curr is not None and i < left - 1:
            prev = curr
            curr = curr.next
            i += 1

        last_node_from_left = prev
        last_node_from_right = curr
        next = None

        i = 0
        while curr is not None and i < right - left + 1:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1
        if last_node_from_left is not None:
            last_node_from_left.next = prev
        else:
            head = prev

        last_node_from_right.next = curr

        return head
