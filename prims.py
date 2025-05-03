import sys

# Function to find the vertex with the minimum key value
def minKey(key, mstSet, V):
    min_val = sys.maxsize
    min_index = -1

    for v in range(V):
        if key[v] < min_val and not mstSet[v]:
            min_val = key[v]
            min_index = v

    return min_index

# Function to print the MST
def printMST(parent, graph, V):
    print("Edge \tWeight")
    for i in range(1, V):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

# Prim's Algorithm
def primMST(graph, V):
    key = [sys.maxsize] * V
    parent = [None] * V
    key[0] = 0
    mstSet = [False] * V

    parent[0] = -1  # First node is root of MST

    for _ in range(V):
        u = minKey(key, mstSet, V)
        mstSet[u] = True

        for v in range(V):
            if graph[u][v] != 0 and not mstSet[v] and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    printMST(parent, graph, V)

# Get user input
V = int(input("Enter the number of vertices: "))
graph = []

print("Enter the adjacency matrix row by row (0 if no edge):")
for i in range(V):
    row = list(map(int, input(f"Row {i}: ").split()))
    graph.append(row)

primMST(graph, V)
