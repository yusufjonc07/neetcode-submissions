class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        top = self.stack[-1]
        self.stack = self.stack[:-1]
        return top

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minN = float('inf')
        for n in self.stack:
            if n < minN:
                minN = n
        return minN

