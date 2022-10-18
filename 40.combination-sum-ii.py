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
        
        def dfs(targe, start = 0, result = []):
            if targe == 0 and result not in results:
                results.append(result.copy())
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > targe:
                    break

                targe = targe - candidates[i]
                result = result + [candidates[i]]
                dfs(targe, i+1, result)
                
        
        dfs(target)
        return results
        
# @lc code=end

candidates = [10,1,2,7,6,1,5]
target = 8

method = Solution()
method.combinationSum2(candidates, target)