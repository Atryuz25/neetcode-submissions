class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        a = 0
        while l<r:
            if heights[l]>heights[r]:
                a = max(a,heights[r]*(r-l))
                r-=1
            elif heights[l]<=heights[r]:
                a = max(a,heights[l]*(r-l))
                l+=1
            

        return a