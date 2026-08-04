class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        s=1
        e = max(piles)
        while s<=e:
            mid = (s+e)//2
            c = 0
            for i in piles:
                c+=math.ceil(i/mid)
            if c<=h:
                e= mid-1
            elif c>h:
                s=mid+1
        return s