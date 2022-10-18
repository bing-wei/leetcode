#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int):
        if dividend == -2147483648 and divisor==-1:
            return 2147483647
        ans = dividend / divisor
        if ans > 0 :
            if ans - round(ans) < 0:
                return round(ans)-1
        if ans < 0 :
            if ans - round(ans) > 0:
                return round(ans)+1
        return round(ans)

# @lc code=end

