class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        output =[]
        vis, cyc = set(), set()

        def dfs(crs):
            if crs in cyc:
                return False
            
            if crs in vis:
                return True
            
            cyc.add(crs)

            for pre in premap[crs]:
                if dfs(pre) == False:
                    return False
                
            cyc.remove(crs)
            vis.add(crs)
            output.append(crs)
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
            
        return output