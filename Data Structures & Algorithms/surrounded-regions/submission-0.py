class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        vis = set()

        def dfs(r,c):
            if(r<0 or c<0 or r>=row or c>=col or (r,c) in vis or board[r][c] == "X"):
                return
            vis.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(row):
            dfs(i,0)
            dfs(i,col-1)

        for j in range(col):
            dfs(0,j)
            dfs(row-1,j)

        for i in range(row):
            for j in range(col):
                if (i,j) not in vis:
                    board[i][j] = "X"
               