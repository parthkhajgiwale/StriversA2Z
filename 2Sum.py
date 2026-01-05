class Solution:
    def twoSum(self, nums, target):
        """
        Problem Statement:
        Given an array of integers nums and an integer target,
        return the indices (0-indexed) of the two numbers such that
        they add up to target.

        Conditions:
        - Each input has exactly one solution
        - The same element cannot be used twice
        - Return indices in increasing order

        Example:
        nums = [1, 6, 2, 10, 3]
        target = 7
        Output: [0, 1]
        Explanation: nums[0] + nums[1] = 1 + 6 = 7
        """

        # Dictionary to store number and its index
        seen = {}

        # Loop through the array
        for i in range(len(nums)):
            current = nums[i]
            needed = target - current  # Value needed to reach target

            # If needed value already exists, we found the pair
            if needed in seen:
                # Return indices in increasing order
                return [seen[needed], i]

            # Store the current number with its index
            seen[current] = i
