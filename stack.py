class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty() == False:
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def peek(self):
        if self.is_empty() == False:
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

    def size(self):
        return len(self.items)

    def reverse(self):
        aux_stack = Stack()

        while self.is_empty() == False:
            item = self.pop()
            aux_stack.push(item)

        self.items = aux_stack.items  

# Example 
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Original Stack:", stack.items)

popped_item = stack.pop()
if popped_item != None:
    print("Popped:", popped_item)
print("Stack:", stack.items)

peeked_item = stack.peek()
if peeked_item != None:
    print("Peek:", peeked_item)

print("Is empty?", stack.is_empty())

print("Stack size:", stack.size())

stack.reverse()
print("Reversed Stack:", stack.items)

