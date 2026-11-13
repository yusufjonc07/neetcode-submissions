class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for m in strs:
            count = [0] * 26
            for c in m:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(m)
        
        return list(res.values())

