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

def bfs(graph, start):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(graph[node])

print("Following is BFS traversal:")
bfs(graph, 's')
