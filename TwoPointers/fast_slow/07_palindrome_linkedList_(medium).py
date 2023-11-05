

if __name__ == '__main__':
    solution = palindrome_linkedlist()

    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    solution.is_palindromic_linkedlist(head)


