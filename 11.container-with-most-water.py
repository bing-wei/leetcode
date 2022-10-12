#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, heights):
        i, j, max_container = 0, len(heights)-1, 0
        while (i<=j):
            if heights[i] <= heights[j]:
                container = (j-i)*min(heights[i],heights[j])
                i += 1 
            else:
                container = (j-i)*min(heights[i],heights[j])
                j -= 1
            if max_container<container: max_container=container
        return max_container

        
        
# @lc code=end

