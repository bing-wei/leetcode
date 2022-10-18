#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums, target):
        nums = list(set(nums))
        return target in nums
# @lc code=end

