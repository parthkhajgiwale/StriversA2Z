def knapsack_01(weights, values, W):
    """
    0/1 Knapsack using DP (no imports).
    Returns: (max_value, chosen_item_indices)
    chosen_item_indices are 0-based.
    """
    n = len(weights)
    if n != len(values):
        raise ValueError("weights and values must have the same length")

    # dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    # Build table
    for i in range(1, n + 1):
        wt = weights[i - 1]
        val = values[i - 1]
        for w in range(W + 1):
            # Option 1: skip item i-1
            best = dp[i - 1][w]
            # Option 2: take item i-1 if it fits
            if wt <= w:
                candidate = val + dp[i - 1][w - wt]
                if candidate > best:
                    best = candidate
            dp[i][w] = best

    # Backtrack to find chosen items
    chosen = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # item i-1 was taken
            chosen.append(i - 1)
            w -= weights[i - 1]

    chosen.reverse()
    return dp[n][W], chosen


# Example usage:
if __name__ == "__main__":
    weights = [1, 2, 3, 4]
    values = [10, 15, 40, 50]
    W = 6

    max_value, chosen_items = knapsack_01(weights, values, W)
    print("Max value:", max_value)
    print("Chosen item indices:", chosen_items)
    # If you want to see the actual items:
    print("Chosen items (weight, value):", [(weights[i], values[i]) for i in chosen_items])
