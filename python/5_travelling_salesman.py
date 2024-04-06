import itertools

def tsp_bruteforce(graph):
    min_distance = float('inf')
    min_path = None
    for path in itertools.permutations(graph.keys()):
        distance = 0
        for i in range(len(path)-1):
            distance += graph[path[i]][path[i+1]]
        distance += graph[path[-1]][path[0]]
        if distance < min_distance:
            min_distance = distance
            min_path = path
    return min_path, min_distance

# Example graph representation (adjacency matrix)
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

min_path, min_distance = tsp_bruteforce(graph)
print("Shortest Path:", min_path)
print("Shortest Distance:", min_distance)
