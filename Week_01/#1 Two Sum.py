class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return 0
        for i in range(len(nums)):
            if (target > 0 and nums[i] <= target) or (target < 0 and nums[i] >= target) or target == 0:
                left_value = target - nums[i]
                if left_value in nums:
                    if i != nums.index(left_value):
                        return [i, nums.index(left_value)]