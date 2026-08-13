class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False


        adj = {i:[] for i in range(n)}
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
            

        vis =set()
        def dfs(x,prev):
            if x in vis:
                return False
            
            vis.add(x)
            for j in adj[x]:
                if j == prev:
                    continue
                if not dfs(j,x):
                    return False
            return True

        return dfs(0,-1) and n == len(vis)