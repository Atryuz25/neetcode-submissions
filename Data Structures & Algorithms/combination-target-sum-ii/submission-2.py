class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums.sort()
        def backtrack(i,path,k):
            if k == target:
                res.append(path[:])
                return
            if i >= len(nums) or k>target:
                return
            

            path.append(nums[i])
            backtrack(i+1,path,k+nums[i])
            path.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1,path,k)

        backtrack(0,[],0)
        return res
 
        
        