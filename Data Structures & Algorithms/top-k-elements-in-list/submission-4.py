class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        count_table = [[] for _ in range(len(nums)+1)]

        for n in nums:
            freq_table[n] = freq_table.get(n, 0) + 1

        for num, freq in freq_table.items():
            count_table[freq].append(num)

        res = []

        for i in range(len(count_table) - 1, 0, -1):
            for e in count_table[i]:
                res.append(e)

                if len(res) == k:
                    return res
        

        return res
