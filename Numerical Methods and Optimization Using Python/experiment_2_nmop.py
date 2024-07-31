class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, new_data):
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
    print("Inserted", new_data, "at the beginning")

  def insert_after(self, prev_node, new_data):
    if prev_node is None:
      print("The given previous node cannot be NULL")
      return
    new_node = Node(new_data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    print("Inserted", new_data, "after", prev_node.data)

  def insert_at_end(self, new_data):
    new_node = Node(new_data)
    if self.head is None:
      self.head = new_node
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node
    print("Inserted", new_data, "at the end")

  def delete_node(self, key):
    temp = self.head
    if temp is not None:
      if temp.data == key:
        self.head = temp.next
        temp = None
        print("Deleted", key)
        return
    while temp is not None:
      if temp.data == key:
        break
      prev = temp
      temp = temp.next
    if temp == None:
      print(key, "not found")
      return
    prev.next = temp.next
    temp = None
    print("Deleted", key)

  def print_list(self):
    temp = self.head
    while temp:
      print(temp.data, end=" ")
      temp = temp.next
    print()

class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def push(self, item):
    self.items.append(item)
    print("Pushed", item)

  def pop(self):
    if self.is_empty():
      print("Stack is empty")
      return None
    item = self.items.pop()
    print("Popped", item)
    return item

  def peek(self):
    if self.is_empty():
      print("Stack is empty")
      return None
    return self.items[-1]

  def display(self):
    if self.is_empty():
      print("Stack is empty")
      return
    print("Stack elements:", self.items)

class Queue:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.append(item)
    print("Enqueued", item)

  def dequeue(self):
    if self.is_empty():
      print("Queue is empty")
      return None
    item = self.items.pop(0)
    print("Dequeued", item)
    return item

  def front(self):
    if self.is_empty():
      print("Queue is empty")
      return None
    return self.items[0]

  def display(self):
    if self.is_empty():
      print("Queue is empty")
      return
    print("Queue elements:", self.items)

# Example usage for LinkedList
llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_beginning(2)
llist.insert_at_end(3)
llist.insert_after(llist.head.next, 4)
print("Created linked list:")
llist.print_list()
llist.delete_node(1)
print("Linked list after deleting 1:")
llist.print_list()

# Example usage for Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()
stack.pop()
print("Top element:", stack.peek())
stack.display()

# Example usage for Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()
queue.dequeue()
print("Front element:", queue.front())
queue.display()

