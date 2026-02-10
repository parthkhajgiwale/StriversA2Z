class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = 0

        for l in range(n):
            even_set = set()
            odd_set = set()

            for r in range(l, n):
                x = nums[r]
                if x % 2 == 0:
                    even_set.add(x)
                else:
                    odd_set.add(x)

                if len(even_set) == len(odd_set):
                    ans = max(ans, r - l + 1)

        return ans
