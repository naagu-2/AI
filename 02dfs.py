graph = {
    's': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['G', 'H'],
    'C': ['E', 'F'],
    'H': [],
    'G': ['I'],
    'E': ['K'],
    'I': [],
    'F': [],
    'D': [],
    'K': []  
}

visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is DFS traversal:")
dfs(visited, graph, 's')
