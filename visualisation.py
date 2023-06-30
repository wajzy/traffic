import matplotlib.pyplot as plt
import CityMap as cm

class VisualizedMap(cm.CityMap):
    def plot_map(self):
        x = []
        y = []
        labels = []
        connections = []

        for vertex, location in self.vertices.items():
            x.append(location['x'])
            y.append(location['y'])
            labels.append(vertex)

        for edge in self.edges.keys():
            connections.append(edge)

        plt.figure(figsize=(8, 8))
        plt.scatter(x, y, color='red')
        for i in range(len(labels)):
            plt.annotate(labels[i], (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha='center')
        for connection in connections:
            start_vertex, end_vertex = connection
            start_location = self.get_vertex_location(start_vertex)
            end_location = self.get_vertex_location(end_vertex)
            plt.plot([start_location['x'], end_location['x']], [start_location['y'], end_location['y']], 'k-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('City Map')
        plt.grid(True)
        plt.show()


# Create an instance of CityMap
map1 = VisualizedMap()

# Add vertices to the map
map1.add_vertex('A', {'x': 5, 'y': 10})
map1.add_vertex('B', {'x': 20, 'y': 5})
map1.add_vertex('C', {'x': 50, 'y': 5})
map1.add_vertex('D', {'x': 60, 'y': 25})
map1.add_vertex('E', {'x': 65, 'y': 30})
map1.add_vertex('F', {'x': 80, 'y': 30})
map1.add_vertex('G', {'x': 100, 'y': 40})
map1.add_vertex('H', {'x': 135, 'y': 100})
map1.add_vertex('I', {'x': 150, 'y': 250})
map1.add_vertex('K', {'x': 180, 'y': 250})
map1.add_vertex('L', {'x': 200, 'y': 200})
map1.add_vertex('M', {'x': 250, 'y': 250})

# Add edges to the map
map1.add_edge('A', 'B', 10)
map1.add_edge('B', 'A', 12)
map1.add_edge('A', 'C', 20)
map1.add_edge('B', 'C', 15)
map1.add_edge('B', 'E', 50)
map1.add_edge('E', 'B', 45)
map1.add_edge('C', 'B', 5)
map1.add_edge('C', 'A', 100)
map1.add_edge('D', 'C', 20)
map1.add_edge('D', 'E', 10)
map1.add_edge('F', 'E', 40)
map1.add_edge('E', 'F', 60)
map1.add_edge('E', 'I', 120)
map1.add_edge('I', 'E', 180)
map1.add_edge('F', 'E', 5)
map1.add_edge('G', 'F', 80)
map1.add_edge('F', 'G', 65)
map1.add_edge('F', 'M', 100)
map1.add_edge('M', 'F', 100)
map1.add_edge('H', 'G', 10)
map1.add_edge('H', 'I', 30)
map1.add_edge('I', 'H', 30)
map1.add_edge('H', 'K', 40)
map1.add_edge('K', 'H', 45)
map1.add_edge('K', 'I', 100)
map1.add_edge('L', 'K', 25)
map1.add_edge('K', 'L', 25)
map1.add_edge('A', 'K', 20)
map1.add_edge('L', 'C', 200)
map1.add_edge('C', 'L', 250)
map1.add_edge('M', 'L', 20)
map1.add_edge('M', 'A', 50)
map1.add_edge('A', 'M', 20)

# Plot the map
map1.plot_map()