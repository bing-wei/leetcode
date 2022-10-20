#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums):
        ans = []
        one_nums = list(set(nums))
        for i in one_nums:
            nums.remove(i)
            if i not in nums:
                ans.append(i)
        return ans
        
# @lc code=end

