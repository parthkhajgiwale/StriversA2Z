class Solution:
    def upperBound(self, nums, x):
        """
        Finds the upper bound index for a given value x in a sorted array.

        Upper Bound:
        The smallest index such that nums[index] > x.
        If no such index exists, return the length of the array.

        Args:
            nums (List[int]): Sorted list of integers
            x (int): Target value

        Returns:
            int: Upper bound index
        """

        # Initialize search boundaries
        left = 0
        right = len(nums) - 1

        # Default answer is length of array
        ans = len(nums)

        # Binary search
        while left <= right:
            mid = (left + right) // 2

            # If current element is strictly greater than x,
            # it could be a valid upper bound
            if nums[mid] > x:
                ans = mid          # Store potential answer
                right = mid - 1    # Search left side for smaller index
            else:
                # If nums[mid] <= x, discard left half
                left = mid + 1

        return ans
