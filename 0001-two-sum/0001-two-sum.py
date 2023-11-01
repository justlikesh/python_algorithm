class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            rest = target - num
            if rest in nums[i+1:]:
                return [nums.index(num) ,nums[i+1:].index(rest)+(i+1)]

        