class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        mheap = [-x for x in stones]
        heapq.heapify(mheap)

        

        while len(mheap)>=2:
            y = heapq.heappop(mheap)
            x = heapq.heappop(mheap)
            print(x,y)
            if x>y:
                y = y-x
                heapq.heappush(mheap,y)
            print(mheap)
        return -mheap[0] if mheap else 0