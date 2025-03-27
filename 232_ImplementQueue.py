class MyQueue:
    
    def __init__(self):
        self.add = []
        self.remove = []

    def push(self, x: int) -> None:
        self.add.append(x)

    def pop(self) -> int:
        if len(self.remove) > 0:
            return self.remove.pop()
        
        while self.add:
            self.remove.append(self.add.pop())
        
        return self.remove.pop()

    def peek(self) -> int:
        if len(self.remove) > 0:
            return self.remove[-1]
        
        while self.add:
            self.remove.append(self.add.pop())
        
        return self.remove[-1]
        

    def empty(self) -> bool:
        if self.add or self.remove: 
            return False
        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()