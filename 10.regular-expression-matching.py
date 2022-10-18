#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start

from re import S


class Solution:
    def isMatch(self, s: str, p: str):
        for i in range(len(p)):
            if p[i] == '*':
                break
            elif p[i] == '.':
                continue
            elif s[i] == p[i]:
                continue
            else:
                return False
        if p[-1] == '.' or p[-1] == '*': return True
        return False
        
# @lc code=end

s = "aab"
p = "c*a*b"

method = Solution()
method.isMatch(s, p)