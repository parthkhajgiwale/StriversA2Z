"""
FIBONACCI USING DYNAMIC PROGRAMMING
----------------------------------
F(n) = F(n-1) + F(n-2)
Base cases:
F(0) = 0
F(1) = 1
"""

# ==========================================================
# METHOD 1: TOP-DOWN DYNAMIC PROGRAMMING (MEMOIZATION)
# ==========================================================

def fibonacci_memo(n, memo=None):
    """
    Top-Down DP (Memoization)

    Idea:
    - Use recursion
    - Store results of subproblems in a dictionary
    - Avoid recomputation

    Time Complexity: O(n)
    Space Complexity: O(n)  [memo + recursion stack]
    """
    if memo is None:
        memo = {}

    # If already computed, return stored value
    if n in memo:
        return memo[n]

    # Base case
    if n <= 1:
        return n

    # Store the computed result
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# ==========================================================
# METHOD 2: BOTTOM-UP DYNAMIC PROGRAMMING (TABULATION)
# ==========================================================

def fibonacci_tab(n):
    """
    Bottom-Up DP (Tabulation)

    Idea:
    - Start from base cases
    - Build the solution iteratively using a DP table

    Time Complexity: O(n)
    Space Complexity: O(n)  [DP table]
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ==========================================================
# METHOD 3: SPACE OPTIMIZED BOTTOM-UP DP
# ==========================================================

def fibonacci_optimized(n):
    """
    Optimized Bottom-Up DP

    Idea:
    - Only last two values are needed
    - No DP table required

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


# ==========================================================
# DRIVER CODE
# ==========================================================

if __name__ == "__main__":
    n = 10
    print("Memoization :", fibonacci_memo(n))
    print("Tabulation  :", fibonacci_tab(n))
    print("Optimized   :", fibonacci_optimized(n))


# ==========================================================
# DIFFERENCE BETWEEN METHOD 1 AND METHOD 2 (COMMENT ONLY)
# ==========================================================

"""
MEMOIZATION (TOP-DOWN):
- Uses recursion
- Solves subproblems only when needed
- Uses extra recursion stack
- Easier to write for recursive problems
- Risk of stack overflow for large n

TABULATION (BOTTOM-UP):
- Uses iteration (loops)
- Solves all subproblems in advance
- No recursion stack
- Better control over memory
- Slightly harder to design but more efficient
"""
