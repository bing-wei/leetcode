#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int):
        if n <= 1:
            return ['()']
        else:
            list1 = ['()']
            for _ in range(n-1):
                list1 = self.add_parentheses(list1)
            return list1

    def add_parentheses(self, list1):
        output = []
        for i in list1:
            for j in range(len(i)):
                final_string = i[:j] + '()' + i[j:]
                if final_string not in output:
                    output.append(final_string)
        return output
 





        
# @lc code=end