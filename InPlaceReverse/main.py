from typing import Optional


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


def reverse(head):
    next = None
    prev = None
    curr = head
    while curr.next != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    curr.next = prev

    return curr


def deleteDuplicates(head: Optional[Node]) -> Optional[Node]:
    curr = head.next
    prev = head
    while curr:
        while curr and prev.data == curr.data:
            curr = curr.next
            continue
        prev.next = curr
        prev = curr
        if curr:
            curr = curr.next
    return head


def mergeTwoLists(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
    ans = Node(0)
    ans_head = ans

    while list1 or list2:
        if list1 and list2 and list1.data > list2.data or list2 is None:
            ans.next = Node(list1.data)
            list1 = list1.next
        else:
            ans.next = Node(list2.data)
    return ans_head.next


if __name__ == '__main__':
    node = Node(1)
    head = node
    nums =[1,1,1,1]

    for num in nums:
        head.next = Node(num)
        head = head.next
    new_head = deleteDuplicates(node)

    while new_head is not None:
        print(new_head.data)
        new_head = new_head.next
