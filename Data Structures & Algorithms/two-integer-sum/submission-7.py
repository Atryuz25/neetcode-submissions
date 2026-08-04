class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di ={}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in di:
                return [di[diff],i]
            di[n]= i

        
                
        