class Solution:
    def numProvinces(self, adj):
        """
        Problem:
        --------
        We are given an undirected graph of n cities as an n x n adjacency matrix `adj`.
        - adj[i][j] == 1 means city i and city j are directly connected
        - adj[i][j] == 0 means not directly connected

        A "province" is a connected component in this undirected graph:
        a group of cities where every city is reachable from every other city
        via direct or indirect connections.

        Goal: Return the number of provinces (connected components).

        Approach (DFS / Graph Traversal):
        -------------------------------
        - Treat each city as a node.
        - If a city has not been visited yet, it starts a new province.
          From that city, run DFS to mark all cities reachable from it as visited.
        - Count how many times we had to start a DFS -> that's the number of provinces.

        Time Complexity:
        ----------------
        - We may scan across a whole row of the adjacency matrix for each node during DFS.
        - O(n^2) time, where n is number of cities.
        - O(n) extra space for the visited array (+ recursion stack; iterative also possible).
        """
        n = len(adj)
        visited = [False] * n  # visited[i] = True if city i is already assigned to some province

        def dfs(city):
            """Mark all cities in the same province as `city` using DFS."""
            visited[city] = True

            # Explore all possible neighbors (because matrix representation)
            for neighbor in range(n):
                # If there's a connection and we haven't visited neighbor, continue DFS
                if adj[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        provinces = 0

        # Each unvisited city starts a new connected component (province)
        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces
