#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height):
        axis = sum(height)
        mix_h = max(height)
        
        for i in range(0,height.index(mix_h)):
            if height[i] > height[i+1]:
                height[i+1] = height[i]

        for i in range(len(height)-1,height.index(mix_h),-1):
            if height[i] > height[i-1]:
                height[i-1] = height[i]
        return sum(height)- axis


        
# @lc code=end