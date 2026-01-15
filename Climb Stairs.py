class Solution:
    """
    Problem: Climbing Stairs

    You are given a staircase with `n` steps.
    You start at step 0 and want to reach step `n`.

    Rules:
    - At each move, you can climb either:
        1 step, or
        2 steps

    Task:
    Return the total number of unique ways to reach the nth step.
    """

    def climbStairs(self, n: int) -> int:
        """
        Approach: Dynamic Programming (Optimized)

        Key Observation:
        - To reach step `n`, you could have come from:
            - step (n - 1) by taking 1 step
            - step (n - 2) by taking 2 steps
        - Therefore:
            ways(n) = ways(n - 1) + ways(n - 2)

        Base Cases:
        - n = 1 → 1 way  (1)
        - n = 2 → 2 ways (1+1, 2)

        This forms a Fibonacci-like sequence.
        We optimize space by keeping only the last two values.

        Time Complexity:  O(n)
        Space Complexity: O(1)
        """

        # Handle small cases directly
        if n <= 2:
            return n

        # dp1 -> ways to reach (n - 2)
        # dp2 -> ways to reach (n - 1)
        dp1, dp2 = 1, 2

        # Build up the solution iteratively
        for _ in range(3, n + 1):
            current = dp1 + dp2
            dp1 = dp2
            dp2 = current

        return dp2
