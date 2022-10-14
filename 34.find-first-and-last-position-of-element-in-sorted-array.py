#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start


class Solution:
    def searchRange(self, nums, target):
        #find left
        i,j = 0,len(nums)-1
        while i <= j:
            mid = int((i + j) / 2)
            if target > nums[mid]: 
                i = mid + 1
            else: 
                j = mid - 1
        left = i

        #find right
        i,j = 0,len(nums)-1
        while i <= j:
            mid = int((i + j) / 2)
            if target >= nums[mid]: 
                i = mid + 1
            else: 
                j = mid - 1
        right = j

        if left <= right:
            return [left, right]
        else:
            return [-1, -1]


        
        


# @lc code=end

