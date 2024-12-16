from collections import deque
class Stack:
    def __init__(self) -> None:
        self.container = deque()
        
    def push(self,data):
        self.container.append(data)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def reverse(self,text):
        return text[::-1]
    

stack = Stack()
stack.push('n')
stack.push('o')
stack.push('x')
stack.push('a')
stack.push('d')
stack.push('a')
stack.push('d')
print(stack.container)
elem = stack.reverse('We will conquere COVID-19')
print(elem)

