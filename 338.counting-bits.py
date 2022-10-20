#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n):
        ans,i = [],0
        while i <= n:
            ans.append(self.count_one(i))
            i+=1
        return ans
    
    def count_one(self, n):
        return n.bit_count()

        
# @lc code=end

