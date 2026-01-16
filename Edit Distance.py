#Given two strings word1 and word2, return the minimum number of operations to convert word1 → word2.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        # dp[j] represents dp[current_row][j]
        # Initialize base case: converting "" -> word2[:j] requires j inserts
        dp = list(range(m + 1))
        
        # Iterate over word1 (rows)
        for i in range(1, n + 1):
            # prev_diag stores dp[i-1][j-1] (diagonal value) as we sweep across j
            prev_diag = dp[0]
            
            # Base case for this row: converting word1[:i] -> "" requires i deletes
            dp[0] = i
            
            # Iterate over word2 (columns)
            for j in range(1, m + 1):
                temp = dp[j]  # dp[j] before overwrite = dp[i-1][j] (value from previous row)
                
                if word1[i - 1] == word2[j - 1]:
                    # Characters match: carry over diagonal (no operation)
                    dp[j] = prev_diag
                else:
                    # Compute costs of the three operations:
                    insert_cost  = dp[j - 1] + 1   # dp[i][j-1] + insert
                    delete_cost  = dp[j] + 1       # dp[i-1][j] + delete  (dp[j] is still previous-row here)
                    replace_cost = prev_diag + 1   # dp[i-1][j-1] + replace
                    
                    dp[j] = min(insert_cost, delete_cost, replace_cost)
                
                # Move diagonal forward for next j
                prev_diag = temp
        
        return dp[m]
