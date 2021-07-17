# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [2,3,0,1,4]
# Output: 2

class Solution:
    def jump(self, nums: List[int]) -> int:
   
#         curr_end=farthest=nums[0]
#         jumps=1
#         n=len(nums)
#         if n==1:
#             return 0
#         for i in range(1,n):
#             if i == n-1:
#                 return jumps
#             farthest = max(farthest, nums[i]+i)
#             if i == curr_end:
#                 jumps +=1
#                 curr_end = farthest
#         return jumps
       
        target,start,end,step=len(nums)-1,0,0,0
        while end < target:
            step += 1
            maxend = end +1
            
            for i in range(start,end+1):
                if i + nums[i] >=target:
                    return step
                maxend = max(maxend, i+nums[i])
            start, end = end+1, maxend
        return step
