class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        x = list(d.values())
        x.sort(reverse = True)
        y=[]
        for j in range(k):
            for q in d:
                if d[q] == x[j] and q not in y:
                    y.append(q)
        return y
    
        