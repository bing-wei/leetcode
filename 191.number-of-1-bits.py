#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n):
        str_n = '{:b}'.format(n)
        ans = 0
        for i in str_n:
            if i == '1':
                ans +=1
        return ans
# @lc code=end

