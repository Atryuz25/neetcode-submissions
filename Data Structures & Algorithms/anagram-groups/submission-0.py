class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for i in strs:
            s = ''.join(sorted(i))
            d[s].append(i)
        return list(d.values())


        