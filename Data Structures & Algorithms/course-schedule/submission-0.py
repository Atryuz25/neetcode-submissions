class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}
        for crs , pre in prerequisites:
            premap[crs].append(pre)
        
        vis = set()

        def dfs(crs):
            if crs in vis:
                return False
            if premap[crs] == []:
                return True
            
            vis.add(crs)
            for i in premap[crs]:
                if not dfs(i): return False
            vis.remove(crs)
            premap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True
        