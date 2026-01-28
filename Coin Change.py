class Solution:
    def coinChange(self, coins, amount):
        """
        Question:
        You are given an array 'coins' representing coins of different denominations
        and an integer 'amount' representing a total amount of money.
        Return the fewest number of coins needed to make up that amount.
        If it is not possible to make the amount, return -1.

        --------------------------------------------------

        Approach (Dynamic Programming):

        1. Use a DP array where dp[x] represents the minimum number of coins
           required to make amount x.
        2. Initialize dp array with a large value to represent infinity.
        3. Base case:
           dp[0] = 0 → 0 coins are needed to make amount 0.
        4. For every amount from 1 to 'amount':
           - Try using each coin.
           - If the coin can be used (x - coin >= 0),
             update dp[x] = min(dp[x], dp[x - coin] + 1).
        5. After filling dp:
           - If dp[amount] is still infinity, return -1.
           - Otherwise, return dp[amount].

        Time Complexity: O(amount × number_of_coins)
        Space Complexity: O(amount)
        """

        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for x in range(1, amount + 1):
            for coin in coins:
                if x - coin >= 0:
                    dp[x] = min(dp[x], dp[x - coin] + 1)

        if dp[amount] == INF:
            return -1
        return dp[amount]
