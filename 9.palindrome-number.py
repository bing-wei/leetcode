#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int):
        s = str(x)
        i,j = 0, len(s)-1
        while i<j:
            if s[i]==s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

# @lc code=end

