class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        vis = set()
        q = deque()
        fresh = 0

        def rot(r,c):
            nonlocal fresh
            if(r<0 or c<0 or r>= row or c>=col or grid[r][c] !=1  or (r,c) in vis):
                return
            fresh -=1
            vis.add((r,c))
            q.append([r,c])
            

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    vis.add((r,c))
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh+=1



        time = 0
        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = 2
                rot(r+1,c)
                rot(r-1,c)
                rot(r,c+1)
                rot(r,c-1)
            time+=1
        return time if fresh == 0 else -1