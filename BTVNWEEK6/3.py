class Stack:
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.stack=[]
    def isEmpty(self):
        return len(self.stack)==0
    def isFull(self):
        return len(self.stack)==self.capacity
    def pop(self):
        if self.isEmpty():
            print("Empty!")
            return None
        return self.stack.pop()
    def push(self,value:int):
        if self.isFull():
            print("Full!")
            return None
        return self.stack.append(value)
    def top(self):
        if self.isEmpty():
            print("Empty!")
            return None
        else:
            return self.stack[-1]
stack = Stack(5)
stack.push(1)
stack.push(9)
stack.push(1)
print(f"Is full? {stack.isFull()}")
print(f"Pop: {stack.pop()}")

print(f"Top: {stack.top()}")