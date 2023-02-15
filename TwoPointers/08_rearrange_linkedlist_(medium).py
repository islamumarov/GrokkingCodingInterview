from node import Node
# https://leetcode.com/problems/reorder-list/description/

class rearrange_linkedlist:
    def reorder(self, head: Node):
        mid = self.mid_node(head)
        reversed_head = self.reverse(mid)
        current = head
        while reversed_head.next:
            tmp = current.next
            current.next = reversed_head
            current = tmp
            rtmp = reversed_head.next
            reversed_head.next = current
            reversed_head = rtmp
        return head

    def mid_node(self, head):
        fast = slow =head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head):
        prev = None
        current = head
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev



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

