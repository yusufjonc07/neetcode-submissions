class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            # pop from stack when parentesis starts to closing
            if c in [']', '}', ')']:
                if stack and ((c == ']' and stack[-1] == '[') or \
                    (c == '}' and stack[-1] == '{') or \
                    (c == ')' and stack[-1] == '(')):
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)

        
        return len(stack)==0



