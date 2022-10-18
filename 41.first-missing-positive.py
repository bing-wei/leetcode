#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums):
        nums = list(set(nums))
        nums.sort()
        max_nums = len(nums)
        max_list = list(range(1, max_nums+2))
        for i in nums:
            if i > 0:
                if i not in max_list:
                    break
                max_list.remove(i)
        return min(max_list)
        
# @lc code=end


nums = [1,2,3,4,5,6,7,8,9,20]
method = Solution()
method.firstMissingPositive(nums)