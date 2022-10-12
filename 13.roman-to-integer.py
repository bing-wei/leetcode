#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str):
        i, sum, s_len = 0, 0, len(s)
        while i < s_len:
            if i+1 < s_len:
                if s[i] == "I" and s[i+1] == "V":
                    i += 2
                    sum+=4
                    continue

                if s[i] == "I" and s[i+1] == "X":
                    i += 2
                    sum+=9
                    continue

                if s[i] == "X" and s[i+1] == "L":
                    i += 2
                    sum+=40
                    continue

                if s[i] == "X" and s[i+1] == "C":
                    i += 2
                    sum+=90
                    continue

                if s[i] == "C" and s[i+1] == "D":
                    i += 2
                    sum+=400
                    continue

                if s[i] == "C" and s[i+1] == "M":
                    i += 2
                    sum+=900
                    continue

            if s[i] == "I":
                i += 1
                sum+=1
                continue

            if s[i] == "I":
                i += 1
                sum+=1
                continue

            if s[i] == "V":
                i += 1
                sum+=5
                continue
            
            if s[i] == "X":
                i += 1
                sum+=10
                continue
            
            if s[i] == "L":
                i += 1
                sum+=50
                continue

            if s[i] == "C":
                i += 1
                sum+=100
                continue

            if s[i] == "D":
                i += 1
                sum+=500
                continue

            if s[i] == "M":
                i += 1
                sum+=1000
                continue
        return sum
# @lc code=end

