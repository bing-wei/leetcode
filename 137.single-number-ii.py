#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
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

