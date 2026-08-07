class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        row = len(heights)
        col = len(heights[0])

        def dfs(r,c,vis,prev):
            if(r<0 or c<0 or r>=row or c>=col or heights[r][c]< prev or (r,c) in vis):
                return
            vis.add((r,c))
            dfs(r+1,c,vis,heights[r][c])
            dfs(r-1,c,vis,heights[r][c])
            dfs(r,c+1,vis,heights[r][c])
            dfs(r,c-1,vis,heights[r][c])
        
        for r in range(row):
            dfs(r,0,pac,heights[r][0])
            dfs(r,col-1,atl,heights[r][col-1])
        for c in range(col):
            dfs(0,c,pac,heights[0][c])
            dfs(row-1,c,atl,heights[row-1][c])
        
        res = []
        for i in range(row):
            for j in range(col):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res
    
            