class Solution:
    def numIslands(self, grid):
        """
        Problem Statement:
        ------------------
        You are given a 2D grid consisting of '1's (land) and '0's (water).
        An island is formed by connecting adjacent lands horizontally or vertically.
        You need to return the total number of islands in the grid.

        Approach:
        ---------
        We use Depth-First Search (DFS) to solve this problem.

        1. Traverse each cell in the grid.
        2. When a cell with value '1' is found, it indicates a new island.
           - Increment the island count.
           - Perform DFS starting from this cell to visit all connected land cells.
        3. During DFS:
           - Mark the current cell as visited by changing '1' to '0'.
           - Recursively visit all 4 possible directions (up, down, left, right).
        4. This ensures that all cells of the same island are visited only once.
        5. Continue scanning the grid until all cells are processed.

        Time Complexity:
        ----------------
        O(rows × cols), since each cell is visited once.

        Space Complexity:
        -----------------
        O(rows × cols) in the worst case due to recursion stack.
        """

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            # Stop if out of bounds or water
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if grid[r][c] == "0":
                return

            # Mark current cell as visited
            grid[r][c] = "0"

            # Visit all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1   # Found a new island
                    dfs(r, c)      # Sink the entire island

        return islands
