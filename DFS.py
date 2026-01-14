def dfs(graph, start):
    """
    Perform Depth-First Search (DFS) on a graph starting from 'start'.

    Approach:
    1. Use a stack (or recursion) to explore as deep as possible before backtracking.
    2. Keep track of visited nodes to avoid infinite loops.
    3. Visit a node, mark it as visited, then recursively visit its neighbors.
    """

    visited = set()  # Keeps track of already visited nodes

    def dfs_helper(node):
        # Step 1: Mark the current node as visited
        visited.add(node)
        print(node)  # Process the node (can be replaced with other logic)

        # Step 2: Visit all unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_helper(neighbor)

    # Step 3: Start DFS from the given start node
    dfs_helper(start)


# Example usage:
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

dfs(graph, 1)
