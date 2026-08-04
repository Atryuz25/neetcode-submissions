class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        p1 = 1
        p2 = 1
        c = 0
        for i in nums:
            if i!=0:
                p1*=i
            elif i==0:
                c+=1
            p2 *= i
        if c>1:
            return([0]*len(nums))
        for i in range(len(nums)):
            if nums[i] == 0:
                l.insert(i,p1)
            else:
                l.insert(i,p2//nums[i])
        return l
            
            
        