#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums):
        ans = len(set(nums))
        nums[:ans] = sorted(set(nums))
        return ans
        
# @lc code=end

