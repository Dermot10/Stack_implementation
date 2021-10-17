from collections import deque

# Basic Implementation of the stack data structure

stack = deque()

# The process of adding elements to the stack
# The collection deque is a more intuitive proecess of utilsing stack
# Resizing of a dynamic array can cause complications with time complexity
stack.append("football")
stack.append("basketball")
stack.append("cricket")
stack.append("baseball")
stack.append("atheletics")
stack.append("rugby")
print(stack)
print(" ")

print("Operating on the principle of Last In First Out \n The last element will be removed")
print(stack.pop())
print(" ")
print(stack)
print(stack.pop())
print(" ")
print("Again the last element from the stack has been removed")
print(stack)
print("")


# Implementation of the stack data structure using OOP principles

class Stack():
    def __init__(self):
        self.buffer = deque()

    def append(self, value):
        self.buffer.append(value)

    def pop(self):
        self.buffer.pop()

    def count(self):
        self.buffer.count()
        return self.buffer.count

    def copy(self):
        self.buffer.copy()
        return self.buffer.copy

    def insert(self):
        self.buffer.insert()

    def clear(self):
        self.buffer.clear()


stack1 = Stack()

stack1.append({
    "Blue": "Skies",
    "Green": "Grass",
    "Brown": "Earth"
})

print(stack1.buffer)
print(" ")

stack1.append({
    "Book": "Mastery",
    "Comics": "Marvel",
    "Manga": "One Piece"
})


print(stack1.buffer)
print("")

stack1.append({
    "Pencils": "Mechanical",
    "Markers": "Copics",
    "Brushes": "Brush Pens"
})

print(stack1.buffer)
print("")

# All of the new elements added to the stack
# Last element removed from the stack

stack1.pop()
print(stack1.buffer)


stack1.append({
    "phone": "1",
    "wallet": "1",
    "keys": "2"
})
print("")
print(stack1.buffer)

# Creating a shallow copy of the deque
print("")
stack1.buffer.copy()
print(stack1.buffer)


# clearing out the contents of the queue
print(" ")
stack1.clear()
print(stack1.buffer)
