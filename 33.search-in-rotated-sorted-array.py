#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums, target) :
        if target in nums:
            return nums.index(target)
        return -1
        
# @lc code=end

