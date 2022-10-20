#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        one_nums = list(set(nums))
        for i in one_nums:
            nums.remove(i)
            if i not in nums:
                return i
        
# @lc code=end

