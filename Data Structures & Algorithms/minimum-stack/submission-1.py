class MinStack:

    def __init__(self):
       self.min_val = -2 ** 31 
       self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_val = val
        else:
            diff = val - self.min_val
            self.stack.append(diff)
            if diff < 0:
                self.min_val = val


    def pop(self) -> None:
        pop = self.stack.pop()
        if pop < 0:
            self.min_val -= pop
        

    def top(self) -> int:
        return self.stack[-1] + self.min_val

    def getMin(self) -> int:
        return self.min_val
        
