class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r,c):
            if (r<0 or c<0 or r>= len(grid) or c>=len(grid[0]) or grid[r][c] == "0" or (r,c) in visited):
                return
            
            visited.add((r,c))
            for dr,dc in directions:
                dfs(r+dr, c+dc)

        island = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    island += 1
                    dfs(i,j)
        return island

                


        