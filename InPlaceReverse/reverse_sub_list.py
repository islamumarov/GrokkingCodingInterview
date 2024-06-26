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


    def reverse_every_k_elements(self, head: Optional[Node], k: int)-> Node:

        if k <= 1 or head is None:
            return head
        current, previous = head, None
        i = 0
        tmp = head
        while tmp is not None:
            tmp = tmp.next
            i += 1
        j = i // k

        while j > 0:
            previous_last = previous
            sub_list_last = current
            next = None

            i = 0

            while current is not None and i < k:
                next = current.next
                current.next = previous
                previous = current
                current = next
                i += 1

            if previous_last is not None:
                previous_last.next = previous
            else:
                head = previous

            sub_list_last.next = current

            if current is None:
                current = head
            previous = sub_list_last
            j -= 1
        return head
