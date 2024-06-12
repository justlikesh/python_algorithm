class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        # init partition index to the last index
        partition_ind = len(nums) - 1

        # for loop until it either goes out of bounds or reaches a index where it is non decreasing
            # the left index would be smaller than the right in which case break
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[partition_ind]:
                break
            else:
                partition_ind = i

        self.reverseArrayPartially(nums, partition_ind, len(nums) - 1)
        if partition_ind == 0:
            return

        target = nums[partition_ind - 1]

        # can replace linear search for smallest num that is bigger than target, but unnecessary complex
        # since there are only 100 length at max

        for i in range(partition_ind, len(nums)):
            if nums[i] > target:
                nums[partition_ind - 1] = nums[i]
                nums[i] = target
                return

    def reverseArrayPartially(self, nums: List[int], left: int, right: int):
        if left < 0 or right >= len(nums):
            print("Index out of bounds")
            return []


        while left < right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp

            left += 1
            right -= 1