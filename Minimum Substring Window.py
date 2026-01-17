# ------------------------------------------------------------
# Problem: Minimum Window Substring
#
# You are given two strings s and t.
# Your task is to find the smallest substring in s that contains
# all the characters of t (including duplicates).
#
# If there is no such substring, return an empty string "".
# The answer is guaranteed to be unique.
#
# Example 1:
# Input:  s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
#
# Example 2:
# Input:  s = "a", t = "a"
# Output: "a"
#
# Example 3:
# Input:  s = "a", t = "aa"
# Output: ""
#
# Constraints:
# - 1 <= len(s), len(t) <= 10^5
# - s and t consist of English letters.
#
# Expected Approach:
# Use a sliding window technique with two pointers and
# frequency counting to achieve an optimal O(n) solution.
# ------------------------------------------------------------


from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        # Frequency map of characters in t
        need = Counter(t)

        # Number of unique characters in t that must be matched
        required_distinct = len(need)

        # Current window character counts
        window = defaultdict(int)

        formed = 0  # How many characters meet required frequency
        l = 0       # Left pointer

        best_len = float("inf")
        best_l = 0
        best_r = 0

        # Expand the window using right pointer
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1

            # Check if current character satisfies requirement
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Try to shrink window when all requirements are met
            while formed == required_distinct:
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                    best_r = r

                left_char = s[l]
                window[left_char] -= 1

                # Window becomes invalid if required char count drops
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                l += 1

        return "" if best_len == float("inf") else s[best_l:best_r + 1]
