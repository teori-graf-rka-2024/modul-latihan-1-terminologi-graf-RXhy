import graph

edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 5)]
G = graph.create_graph(edges)

print(graph.get_degree(G,2))

print(graph.bfs_traversal(G,1))

print(graph.dfs_traversal(G,1))

print(graph.find_shortest_path(G, 1, 4))

graph.visualize_graph(G)