# Problem: Count number of Nice subarrays
# Given an array nums and an integer k.
# A subarray is called "nice" if and only if it contains exactly k odd numbers.
# Return the number of nice (continuous) subarrays.
#
# Example 1:
# nums = [1, 1, 2, 1, 1], k = 3  -> 2
#
# Example 2:
# nums = [4, 8, 2], k = 1 -> 0


from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        Approach:
        Convert each number to 1 if it's odd else 0.
        Then the task becomes: count subarrays whose sum is exactly k.

        We'll use a prefix-sum + hashmap (frequency map):
        - Let prefix = sum of odds seen so far.
        - For each position, number of subarrays ending here with exactly k odds
          equals frequency of (prefix - k) seen before.
        """
        freq = {0: 1}  # prefix_sum -> count (prefix sum 0 occurs once before we start)
        prefix = 0
        ans = 0

        for x in nums:
            prefix += (x & 1)  # add 1 if odd, 0 if even
            ans += freq.get(prefix - k, 0)
            freq[prefix] = freq.get(prefix, 0) + 1

        return ans
