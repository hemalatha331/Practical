class Node:
    def __init__(self, val):
        self.val = val
        self.link = None

def display(head):
    p = head
    while p!=None:
        print(p.val)
        p = p.link

def prepend(head, val):
    new_node = Node(val)
    new_node.link = head
    return new_node

def remove(head, val_to_remove):
    if head == None:
        return None

    if head.val == val_to_remove:
        return head.link

    p = head
    while p.link != None:
        if p.link.val == val_to_remove:
            p.link = p.link.link
            return head
        p = p.link

    return head

# Create the initial linked list
head = Node(1)
head.link = Node(2)
head.link.link = Node(3)
head.link.link.link = Node(5)
print("Before prepending and removing...")
display(head)

print("Prepending....")
head = prepend(head, 7)
head = prepend(head, 8)
print("After prepending...")
display(head)

print("Removing ...")
head = remove(head, 2)
head = remove(head, 1)
print("After removing ...")
display(head)

