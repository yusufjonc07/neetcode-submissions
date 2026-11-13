class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        top, bot = 0, rows-1

        while top <= bot:
            row = (bot+top) // 2

            if matrix[row][-1] < target:
                top = row+1
            elif matrix[row][0] > target:
                bot = row-1
            else:
                break

        if not top <= bot: return False
        
        l, r = 0, len(matrix[row])-1

        while l <= r:
            mid = (r+l) // 2

            if matrix[row][mid] < target:
                l = mid+1
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                return True

        return False