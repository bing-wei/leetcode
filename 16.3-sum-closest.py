#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums, target):
        nums_len = len(nums)
        nums.sort(reverse=True)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(0,nums_len-2):
            j, k = i+1, len(nums)-1
            while j < k:
                s =  nums[i] + nums[j] + nums[k]
                if s > target:
                    j += 1
                elif s < target:
                    k -= 1
                elif s == target:
                    return s 
                if abs(s-target) < abs(ans-target): ans = s
        return ans


test1 = [4,0,5,-5,3,3,0,-4,-5]
test2 = -2
method = Solution()
print(method.threeSumClosest(test1,test2))