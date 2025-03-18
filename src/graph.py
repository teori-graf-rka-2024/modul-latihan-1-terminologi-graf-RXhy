import networkx as nx
import matplotlib.pyplot as plt

def create_graph(edges:list[tuple[int,int]]):
    G  = nx.Graph()
    G.add_edges_from(edges)
    return G

def get_degree(G: nx.Graph, node: int) -> int:
    return G.degree(node)

def dfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.dfs_preorder_nodes(G,start))

def bfs_traversal(G: nx.Graph, start: int) -> list[int]:
    return list(nx.bfs_tree(G,start))    

def find_shortest_path(G: nx.Graph, source: int, target: int) -> list[int]:
    return list(nx.shortest_path(G,source,target))

def visualize_graph(G: nx.Graph) -> None:
    nx.draw(G, nx.spring_layout(G), with_labels=True, node_color='lightblue', edge_color='green', node_size=800)
    plt.savefig("testgraph.png",format="png",dpi=300)
    plt.show()