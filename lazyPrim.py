import random
import heapq
from collections import defaultdict


n = int(input("Enter the height of the maze: "))# Höhe des MST
m = int(input("Enter the width of the maze: ")) # Breite des MST

def generate_grid_edges(n, m):  # Erstelle eine Liste von Kanten für alle Zellen im Gitter
   
    edges = []
    
    def node_id(x, y):
        return y * m + x # Einmalige ID für Koordinate (x, y)
    
    for y in range(n):
        for x in range(m):
            current_id = node_id(x, y)

            # Kante rechts
            if x < m - 1:
                neighbor = node_id(x + 1, y)
                weight = random.randint(1, 24)  # zufaelliges Gewicht des Knotens
                edges.append((current_id, neighbor, weight))  # Kante von current_id zu neighbor mit Gewicht

            # Kanten unten
            if y < n - 1:
                neighbor = node_id(x, y + 1)
                weight = random.randint(1, 24)
                edges.append((current_id, neighbor, weight))
    
    return edges

def build_adjacency_list(edges):  # Erstelle eine Adjazenzliste aus den Kanten
    adj = defaultdict(list)  # Standardwert ist eine leere Liste
    for u, v, weight in edges:
        adj[u].append((v, weight)) # Füge Kante u -> v mit Gewicht zur Adjazenzliste hinzu
        adj[v].append((u, weight)) # Füge Kante v -> u mit Gewicht zur Adjazenzliste hinzu
    return adj


def lazy_prim(adj, start_node):  # Lazy Prim Algorithmus zur Erstellung des minimalen Spannbaums (MST)
    visited = set()  # Menge der besuchten Knoten
    mst_edges = []  # Kanten des minimalen Spannbaums
    edge_queue = []  # Prioritätswarteschlange für Kanten
    mst_weight = 0  # Gewicht des minimalen Spannbaums

    def add_edges(node):  # Füge Kanten des Knotens zur Warteschlange hinzu
        visited.add(node)
        for neighbor, weight in adj[node]:
            if neighbor not in visited:
                heapq.heappush(edge_queue, (weight, node, neighbor)) # Füge Kante zur Warteschlange hinzu
                
    
    add_edges(start_node)  # Füge Kanten des Startknotens zur Warteschlange hinzu

    while edge_queue and len(visited) < len(adj):
        weight, u, v = heapq.heappop(edge_queue)
        if v not in visited:
            mst_edges.append((u, v, weight)) # Füge Kante zum MST hinzu
            mst_weight += weight
            add_edges(v)  # Füge Kanten des neuen Knotens zur Warteschlange hinzu

    return mst_edges  



# Pipeline zur Erstellung des MST
edges = generate_grid_edges(n, m)  # Erstelle Kanten für das Gitter
adj = build_adjacency_list(edges)  # Erstelle Adjazenzliste aus Kanten
max_node = n * m - 1  
start_node = random.randint(0, max_node)  # Wähle zufälligen Startknoten


print(f"Start node: {start_node}")  # Ausgabe des Startknotens
mst_edges = lazy_prim(adj, start_node)  # Erstelle MST mit Lazy Prim Algorithmus

print("Edges in the MST:")
for u, v, weight in mst_edges:  # Ausgabe der Kanten im MST
    print(f"({u}, {v}) with weight {weight}")

print(f"Total weight of the MST: {sum(weight for _, _, weight in mst_edges)}")  # Ausgabe des Gesamtgewichts des MST

while True:
    question = input("Repeat the algorithm? (Press Enter to continue, or type 'no' to exit): ")
    if question.lower() == 'no':
        break

    
    start_node = random.randint(0, max_node)

    print(f"Start node: {start_node}")
    mst_edges = lazy_prim(adj, start_node)

    print("Edges in the MST:")
    for u, v, weight in mst_edges:
        print(f"({u}, {v}) with weight {weight}")

    print(f"Total weight of the MST: {sum(weight for _, _, weight in mst_edges)}")
