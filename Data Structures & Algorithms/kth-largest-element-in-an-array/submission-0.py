class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mnums = [x for x in nums]
        heapq.heapify(mnums)

        while len(mnums)>k:
            heapq.heappop(mnums)
        
        return mnums[0]

        
        