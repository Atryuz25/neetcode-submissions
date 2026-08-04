class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        longest=0
        for i in a:
            if(i-1 not in a):
                length = 1
                while i+1 in a:
                    length +=1
                    i+=1
                longest = max(longest,length)
        return longest
