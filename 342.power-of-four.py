#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int):
        power = 0
        while 4**power <= n:
            if 4**power == n:
                return True
            power += 1
        return False
        
# @lc code=end

