class Solution:
    def lowerBound(self, nums, x):
        """
        Finds the lower bound index for a given value x in a sorted array.

        Lower Bound:
        The smallest index such that nums[index] >= x.
        If no such index exists, return the length of the array.

        Args:
            nums (List[int]): Sorted list of integers
            x (int): Target value

        Returns:
            int: Lower bound index
        """

        # Initialize search boundaries
        left = 0
        right = len(nums) - 1

        # Default answer is length of array (if x is greater than all elements)
        ans = len(nums)

        # Binary search
        while left <= right:
            mid = (left + right) // 2

            # If current element is greater than or equal to x,
            # it could be a valid lower bound
            if nums[mid] >= x:
                ans = mid          # Store potential answer
                right = mid - 1    # Try to find a smaller index on the left
            else:
                # If nums[mid] < x, discard left half
                left = mid + 1

        return ans
