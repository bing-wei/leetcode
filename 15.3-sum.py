#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums):
        nums_len = len(nums)
        ans = []
        nums.sort(reverse=True)
        for i in range(0,nums_len-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                s =  nums[i] + nums[j] + nums[k]
                if s > 0:
                    j += 1
                elif s < 0:
                    k -= 1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                    j += 1; k -= 1
        return ans
        
# @lc code=end

test = [-1,0,1,2,-1,-4]
modthod = Solution()
modthod.threeSum(test)