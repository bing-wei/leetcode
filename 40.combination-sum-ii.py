#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        results = [] 
        result = []

        def dfs(targe,start):
            if targe == sum(result) and result not in results:
                results.append(result.copy())
            elif sum(result) > targe:
                return

            for i in range(start, len(candidates)):
                result.append(candidates[i])
                dfs(targe,i+1)
                result.pop()
        
        dfs(target, 0)
        return results
        
# @lc code=end

candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27

method = Solution()
method.combinationSum2(candidates, target)