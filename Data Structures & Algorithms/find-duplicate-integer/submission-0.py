class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = []
        for n in nums:
            if n in hashmap:
                return n
            hashmap.append(n)

        return False