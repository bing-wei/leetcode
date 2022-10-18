#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        last_num = []
        for i in range(len(matrix)):
            last_num.append(matrix[i][-1] >= target)
        if sum(last_num) <= 0:
            return False
        fix_index = last_num.index(True)
        fix_row  = matrix[fix_index]
        for i in fix_row:
            if i == target:
                return True
        return False
        
# @lc code=end
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
method = Solution()
method.searchMatrix(matrix,target)