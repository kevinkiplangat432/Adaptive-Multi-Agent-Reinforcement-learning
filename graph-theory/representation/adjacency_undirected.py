# Adjacency representation of undirected Graph as Adjacency Matrix

def createGraph(V, edges):
    matrix = [[0 for _ in range(V)] for _ in range(V)]

    # Add each edge to the adjacency matrix 
    for it in edges:
        u = it[0]
        v = it[1]
        matrix[u][v] = 1

        # since the graph is undirected
        matrix[v][u] = 1
    return matrix


if __name__ == "__main__":
    V = 3

    # list of edges (u, v)
    edges = [[0,1], [0,2], [1,2]]

    # build the graph using edges
    matrix = createGraph(V, edges)

    print("Adajacency Matrix Representation:")
    for i in range(V):
        for j in range(V):
            print(matrix[i][j], end=" ")
        print()