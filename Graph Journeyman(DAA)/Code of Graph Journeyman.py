import networkx as nx
import matplotlib.pyplot as plt

# Create a graph object using NetworkX
graph = nx.Graph()

# Function to add a vertex (city)
def add_city(city):
    graph.add_node(city)

# Function to add an edge with distance (between cities)
def add_distance(city1, city2, distance):
    graph.add_edge(city1, city2, weight=distance)

# DFS algorithm
def dfs(graph, start):
    visited = set()
    traversal = []

    def dfs_recursive(node):
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            for neighbor in graph.neighbors(node):
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return traversal

# BFS algorithm
def bfs(graph, start):
    visited = set([start])
    traversal = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        traversal.append(node)
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal

# Kruskal’s algorithm for Minimum Spanning Tree
def kruskal_mst(graph):
    mst = nx.minimum_spanning_tree(graph, algorithm='kruskal')
    return mst

# Prim’s algorithm for Minimum Spanning Tree
def prim_mst(graph):
    mst = nx.minimum_spanning_tree(graph, algorithm='prim')
    return mst

# Function to display the graph visually using matplotlib
def display_graph(graph):
    plt.ion()  # Enable interactive mode
    pos = nx.spring_layout(graph)  # Positioning the nodes
    labels = nx.get_edge_attributes(graph, 'weight')  # Edge weights as labels
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_color='black')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)  # Displaying edge weights
    plt.title("Graph Visualization")
    plt.show()

# Main function to handle user input
def main():
    while True:
        print("\nGraph Journeyman - Terminal Version")
        print("1. Add Cities and Distances")
        print("2. Perform DFS")
        print("3. Perform BFS")
        print("4. Kruskal's Minimum Spanning Tree")
        print("5. Prim's Minimum Spanning Tree")
        print("6. Display Graph")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                city1 = input("Enter the name of the first city (or type 'done' to stop): ")
                if city1.lower() == 'done':
                    break
                city2 = input("Enter the name of the second city: ")
                distance = float(input(f"Enter the distance between {city1} and {city2}: "))
                add_city(city1)
                add_city(city2)
                add_distance(city1, city2, distance)
                print(f"Distance of {distance} added between {city1} and {city2}.")

        elif choice == '2':
            start = input("Enter the starting city for DFS: ")
            if start in graph.nodes:
                dfs_result = dfs(graph, start)
                print("DFS Traversal: ", " -> ".join(dfs_result))
            else:
                print(f"City {start} not found in the graph!")

        elif choice == '3':
            start = input("Enter the starting city for BFS: ")
            if start in graph.nodes:
                bfs_result = bfs(graph, start)
                print("BFS Traversal: ", " -> ".join(bfs_result))
            else:
                print(f"City {start} not found in the graph!")

        elif choice == '4':
            mst = kruskal_mst(graph)
            print("Kruskal's Minimum Spanning Tree:")
            for u, v, data in mst.edges(data=True):
                print(f"{u} -- {v} : {data['weight']}")

        elif choice == '5':
            mst = prim_mst(graph)
            print("Prim's Minimum Spanning Tree:")
            for u, v, data in mst.edges(data=True):
                print(f"{u} -- {v} : {data['weight']}")

        elif choice == '6':
            print("\nGraph vertices (Cities): ", graph.nodes())
            print("Graph edges (Distances): ")
            for u, v, data in graph.edges(data=True):
                print(f"{u} -- {v} : {data['weight']}")
            
            # Call the function to display the graph visually
            display_graph(graph)

            input("Press Enter to return to the main menu...")  # Pause to allow user to see the graph

        elif choice == '7':
            print("Exiting Graph Journeyman.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
