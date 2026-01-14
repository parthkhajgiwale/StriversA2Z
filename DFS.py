def dfs(graph, start, n):
    """
    Perform Depth-First Search (DFS) using a boolean visited array.

    Approach:
    1. Create a visited array of size 'n', initialized to False.
       - False → node not visited
       - True  → node already visited
    2. Start DFS from the given start node.
    3. Mark the node as visited before exploring its neighbors.
    4. Recursively visit all unvisited neighbors.
    """

    visited = [False] * n  # Step 1: Initialize all nodes as unvisited

    def dfs_helper(node):
        # Step 2: Mark current node as visited
        visited[node] = True
        print(node)  # Process the node

        # Step 3: Visit all unvisited neighbors
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs_helper(neighbor)

    # Step 4: Start DFS
    dfs_helper(start)


# Example usage (0-based indexing):
graph = [
    [1, 2],    # neighbors of node 0
    [3, 4],    # neighbors of node 1
    [],        # neighbors of node 2
    [],        # neighbors of node 3
    []         # neighbors of node 4
]

dfs(graph, start=0, n=5)
