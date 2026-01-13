class Solution:
    def selectionSort(self, nums):
        n = len(nums)
        
        for i in range(n):
            # Assume the min is at the start of unsorted part
            min_index = i
            
            # Find the minimum element in the unsorted part
            for j in range(i + 1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            
            # Swap the found minimum with the first unsorted element
            nums[i], nums[min_index] = nums[min_index], nums[i]
        
        return nums
