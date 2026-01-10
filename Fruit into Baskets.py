class Solution:
    def totalFruits(self, fruits):
        """
        Question:
        There is a row of fruit trees represented by an array `fruits`,
        where fruits[i] is the type of fruit on the i-th tree.

        Rules:
        1) You have only two baskets, and each basket can store only ONE type of fruit.
        2) Each basket has unlimited capacity.
        3) You can start picking from any tree, but once started you must move to the right,
           picking exactly one fruit from each tree.
        4) If you encounter a fruit type that cannot fit into the two baskets, you must stop.

        Task:
        Return the maximum number of fruits you can pick following these rules.

        Example:
        Input: fruits = [1, 2, 1]
        Output: 3
        """

        # ---------------------------------------------------------
        # Approach (Sliding Window with at most 2 distinct elements)
        # ---------------------------------------------------------
        # This problem is equivalent to finding the longest contiguous
        # subarray that contains at most 2 distinct fruit types.
        #
        # We use a sliding window:
        # - Expand the right pointer to include fruits[right].
        # - Keep a dictionary to count fruit frequencies in the window.
        # - If the window contains more than 2 distinct fruits,
        #   shrink it from the left until only 2 types remain.
        # - Track the maximum window size during the process.
        #
        # Time Complexity: O(n)
        # Space Complexity: O(1) (at most 2 fruit types in the dictionary)
        # ---------------------------------------------------------

        from collections import defaultdict

        left = 0
        fruit_count = defaultdict(int)
        max_fruits = 0

        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1

            # If more than 2 fruit types, shrink the window
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            # Update maximum fruits collected
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
