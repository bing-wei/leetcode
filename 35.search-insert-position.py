#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums, target):
        if target in nums :
            return nums.index(target)
        else:
            i,j = 0,len(nums)-1
            while i <= j:
                mid = int((i + j) / 2)
                if target > nums[mid]: 
                    i = mid + 1
                else: 
                    j = mid - 1
            return i 

        
# @lc code=end

