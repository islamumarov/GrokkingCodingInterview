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



if __name__ == '__main__':
    node = Node(0)
    head = node
    nums = [1,2,3,4,5,6,7,8,9]

    for num in nums:
        head.next = Node(num)
        head = head.next
    new_head = reverse(node)

    while new_head.next is not None:
        print(new_head.data)
        new_head = new_head.next

