#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from unittest import result


class Solution:
    def combinationSum(self, candidates, target) :
        results = [] 
        result = []

        def dfs(targe,start):
            if targe == sum(result):
                results.append(result.copy())
            elif sum(result) > targe:
                return

            for i in range(start, len(candidates)):
                result.append(candidates[i])
                dfs(targe,i)
                result.pop()
        
        dfs(target, 0)
        return results




# @lc code=end

