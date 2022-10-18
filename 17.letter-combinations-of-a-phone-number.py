#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str):
        ans = []
        for n in digits:
            if n =='2':
                ans = self.list_concat(ans,['a','b','c'])
            if n =='3':
                ans = self.list_concat(ans,['d','e','f'])
            if n =='4':
                ans = self.list_concat(ans,['g','h','i'])
            if n =='5':
                ans = self.list_concat(ans,['j','k','l'])
            if n =='6':
                ans = self.list_concat(ans,['m','n','o'])
            if n =='7':
                ans = self.list_concat(ans,['p','q','r','s'])
            if n =='8':
                ans = self.list_concat(ans,['t','u','v'])
            if n =='9':
                ans = self.list_concat(ans,['w','x','y','z'])
        return ans
    
    def list_concat(self,list1,list2):
        output = []
        if list1 == []:
            return list2
        if list2 == []:
            return list1
        for i in list1:
            for j in list2:
                output.append(i+j)
        return output

        
            

# @lc code=end
digits = "23"
method = Solution()
method.letterCombinations(digits)
