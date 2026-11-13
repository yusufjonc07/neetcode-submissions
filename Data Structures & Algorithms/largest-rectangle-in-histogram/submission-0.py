class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        lRec = 0

        for i, h in enumerate(heights):
            start=i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                lRec = max(lRec, height*(i-index)) 
                start=index

            stack.append((start, h))

        for i, h in stack:
            lRec = max(lRec, h*(len(heights)-i))

        return lRec
