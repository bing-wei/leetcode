#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]
        
# @lc code=end
