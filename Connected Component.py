class Solution:
    def findNumberOfComponent(self, V, edges):
        """
        Problem Statement:
        Given an undirected graph with V vertices (0 to V-1) and a list of undirected edges,
        count how many connected components exist.

        Two vertices u and v are in the same connected component if there is a path between them.

        Example:
        V = 4, edges = [[0,1],[1,2]]  -> components are {0,1,2} and {3} => answer = 2
        """

        # ------------------------------------------------------------
        # Approach (BFS/DFS Graph Traversal):
        # - Build an adjacency list for the undirected graph.
        # - Maintain a visited array to track explored vertices.
        # - For each vertex not visited:
        #     - It starts a new connected component.
        #     - Run BFS/DFS from it to mark all reachable vertices visited.
        # - Count how many times we start a new BFS/DFS => number of components.
        #
        # Time Complexity:  O(V + E)  (each vertex and edge processed a constant number of times)
        # Space Complexity: O(V + E) for adjacency list + O(V) visited
        # ------------------------------------------------------------

        # Build adjacency list
        adj = [[] for _ in range(V)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = [False] * V

        def dfs(start):
            # Iterative DFS to avoid recursion depth issues
            stack = [start]
            visited[start] = True
            while stack:
                node = stack.pop()
                for nei in adj[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

        components = 0
        for v in range(V):
            if not visited[v]:
                components += 1
                dfs(v)

        return components
