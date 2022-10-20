#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int):
        s = ''
        while num >= 1000:
            num-=1000
            s+='M'
        while num >= 500:
            num-=500
            s+='D'
        while num >= 100:
            num-=100
            s+='C'
        while num >= 50:
            num-=50
            s+='L'
        while num >= 10:
            num-=10
            s+='X'
        while num >= 5:
            num-=5
            s+='V'
        while num >= 1:
            num-=1
            s+='I'
        s = s.replace("DCCCC", "CM")
        s = s.replace("CCCC", "CD")
        s = s.replace("LXXXX", "XC")
        s = s.replace("XXXX", "XL")
        s = s.replace("VIIII", "IX")
        s = s.replace("IIII", "IV")
        return s
# @lc code=end

