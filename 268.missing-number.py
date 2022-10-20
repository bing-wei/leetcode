#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums):
        i = 0
        nums.sort()
        while i < nums[-1]:
            if i == nums[i]:
                i += 1
                continue
            return i 
        return nums[-1] + 1 

        
# @lc code=end

