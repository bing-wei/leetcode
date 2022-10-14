#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums, val):
        ans = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ans] = nums[i]
                ans +=1
        return ans
        
# @lc code=end

