class Solution:
    def searchRange(self, nums, target):
        """
        Finds the first and last position of a target value in a sorted array.
        If target is not found, returns [-1, -1].

        Args:
            nums (List[int]): Sorted list of integers
            target (int): Target value

        Returns:
            List[int]: [first_occurrence, last_occurrence]
        """

        # Find first and last occurrence using binary search
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        return [first, last]

    def findFirst(self, nums, target):
        """
        Binary search to find the first occurrence of target.
        """
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid          # Store index
                right = mid - 1    # Move left to find earlier occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans

    def findLast(self, nums, target):
        """
        Binary search to find the last occurrence of target.
        """
        left, right = 0, len(nums) - 1
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                ans = mid          # Store index
                left = mid + 1     # Move right to find later occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans
