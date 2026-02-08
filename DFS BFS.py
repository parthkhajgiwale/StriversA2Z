def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)   # dequeue
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# -------- Main Script --------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
choice = input("Enter traversal type (BFS / DFS): ").strip().upper()

match choice:
    case "BFS":
        print("BFS Traversal:")
        bfs(graph, start_node)

    case "DFS":
        print("DFS Traversal:")
        dfs(graph, start_node)

    case _:
        print("Invalid choice. Please enter BFS or DFS.")
