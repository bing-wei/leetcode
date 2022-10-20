#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n):
        str_n ='{0:032b}'.format(n)
        res_n = str_n[::-1]
        return int(res_n,2)
# @lc code=end

