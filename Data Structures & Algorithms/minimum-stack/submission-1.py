class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            curMin = min(val, self.stack[-1][1])
            self.stack.append((val, curMin))

    def pop(self) -> None:
        top = self.stack[-1][0]
        self.stack = self.stack[:-1]
        return top

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

