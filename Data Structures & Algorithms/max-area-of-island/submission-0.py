class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        vis =  set()

        def dfs(x,y):
            if (x<0 or y<0 or x==row or y==col or grid[x][y]==0 or (x,y)in vis):
                return 0
            
            vis.add((x,y))
            return(1+ dfs(x+1,y)+dfs(x,y+1)+dfs(x+1,y+1)+dfs(x-1,y)+dfs(x,y-1))

        area = 0

        for i in range(row):
            for j in range(col):
                area = max(area,dfs(i,j))
        return area