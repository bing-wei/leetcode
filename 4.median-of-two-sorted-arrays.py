#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums_list = nums1 + nums2
        odd = len(nums_list)%2
        _median = int(len(nums_list)/2)
        nums_list.sort()
        if odd == 1 :
            median = nums_list[_median]
            return median
        elif odd == 0 :
            median = (nums_list[_median-1] + nums_list[_median])/2
            return median
        else:
            return None
# @lc code=end

nums1 = [1,2]
nums2 = [3,4]
method = Solution()
method.findMedianSortedArrays(nums1,nums2)

