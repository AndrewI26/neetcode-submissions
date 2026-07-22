class MinStack:

    # 1 1 -1
    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack = [val]
            self.min = val
        else:
            diff = val - self.min
            if diff < 0:
                self.min = val
                self.stack += [diff]


    def pop(self) -> None:
        diff  = self.stack.pop()
        if diff < 0:
            self.min -= diff

    def top(self) -> int:
        return self.min + self.stack[-1]

    def getMin(self) -> int:
        return self.min
        
