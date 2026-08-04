class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        x = self.stack[len(self.stack)-1]
        return(x)
        

    def getMin(self) -> int:
        return(min(self.stack))
        
