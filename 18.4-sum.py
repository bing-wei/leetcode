#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums, target) :
        nums.sort(reverse=True)
        ans = []
        for i in range(0,len(nums)-3):
            if i>0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>(i+1) and nums[j-1] == nums[j]:
                    continue
                k,l = j+1,len(nums)-1
                while k<l :
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum > target:
                        k += 1
                    elif sum < target:
                        l -= 1
                    elif sum == target:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        while k < l and nums[k] == nums[k+1]:
                            k+=1
                        while k < l and nums[l] == nums[l-1]:
                            l-=1
                        k+=1; l-=1
        return ans

        
# @lc code=end
nums = [1,0,-1,0,-2,2]
target = 0
method = Solution()
method.fourSum(nums,target)
