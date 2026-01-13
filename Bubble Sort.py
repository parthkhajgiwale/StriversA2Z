class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            # After each pass, last i elements are in place
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]  # swap adjacent
        return nums
