def createGraph(V, edges):
    adj = [[] for _ in range(V)]

    # add each edge to the adjacency list 
    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)

        # since the graph is undirected 
        adj[v].append(u)
    return adj


if __name__ == "__main__":
    V = 3

    # list of edges (u, v)
    edges = [[0,1], [0,2], [1,2]]

    # build the graph using edges
    adj = createGraph(V, edges)

    print("adjacency List Representation")
    for i in range(V):

        # print the vertex 
        print(f"{i}:", end=" ")
        for j in adj[i]:

            # print its adjacent
            print(j, end=" ")
        print()