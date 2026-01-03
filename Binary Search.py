class Solution:
    def search(self, nums, target):
        """
        Performs Binary Search on a sorted array.

        Args:
            nums (List[int]): Sorted list of integers
            target (int): Value to search for

        Returns:
            int: Index of target if found, otherwise -1
        """

        # Initialize two pointers
        left = 0
        right = len(nums) - 1

        # Continue searching while the search space is valid
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2

            # If target is found, return its index
            if nums[mid] == target:
                return mid

            # If target is greater, ignore left half
            elif nums[mid] < target:
                left = mid + 1

            # If target is smaller, ignore right half
            else:
                right = mid - 1

        # Target was not found in the array
        return -1
