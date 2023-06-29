import random

class CityMap:
    def __init__(self): #Constructor of the function, sets the initial values for the data#
        self.vertices = {} #Points on the map
        self.edges = {} #Lines between the points on the map
        #self.vertex_data = {}
        #self.edge_data = {}
        self.traffic_lights = set()

    def add_vertex(self, vertex, location=None): #Function to add a point to the map
        self.vertices[vertex] = location #Add the specified location to the specified point within 'vertices' (as a dictionary entry)

    def remove_vertex(self, vertex): #Function to remove a point from the map
        del self.vertices[vertex] #Remove the specified vertex from 'vertices'
        self.edges = {k: v for k, v in self.edges.items() if vertex not in k} #Remove any edges connected to the vertex

    def add_edge(self, start_vertex, end_vertex, weight, additional_info=None): #Function to add edges between vertexes
        if start_vertex not in self.vertices or end_vertex not in self.vertices: #Check if specified edge's vertexes exist already
            raise ValueError("Start or end vertex does not exist in the map.")
        self.edges[(start_vertex, end_vertex)] = {'weight': weight, 'info': additional_info} #For the start and end point tuple's location, add weight and other informational dictionary (as a dictionary entry-->I.e. x={(1,2):{weight:2,info:info}})

    def remove_edge(self, start_vertex, end_vertex): #Function to remove edges between vertexes
        del self.edges[(start_vertex, end_vertex)]

    def get_vertices(self): #Returns the keys for the vertices (practically a list of all the vertices, without their locations)
        return list(self.vertices.keys())

    def get_edges(self): #Returns the keys for the edges (practically a list of all the connections between the vertices, without their weight or info)
        return list(self.edges.keys())

    def get_vertex_location(self, vertex): #Returns the location of a specific vertex
        return self.vertices[vertex]

    def add_traffic_light(self, vertex): #Adds traffic lights to the specified vertex
        self.traffic_lights.add(vertex)

    def remove_traffic_light(self, vertex): #Removes traffic lights from the specified vertex
        self.traffic_lights.discard(vertex)

    def has_traffic_light(self, vertex): #Returns a boolean which tells whether the specified vertex has a traffic light or not
        return vertex in self.traffic_lights

    def get_edge_weight(self, start_vertex, end_vertex): #Returns the weight of a specific edge
        return self.edges[(start_vertex, end_vertex)]['weight']

    def get_edge_info(self, start_vertex, end_vertex): #Returns the information of a specific edge
        return self.edges[(start_vertex, end_vertex)]['info']

    def get_neighbors(self, vertex): #Function that returns the neighbors of a specific edge
        neighbors = []
        for (start_vertex, end_vertex) in self.edges.keys():
            if start_vertex == vertex:
                neighbors.append(end_vertex)
        return neighbors

map1=CityMap() #Create a variable to be modified by the commands

map1.add_vertex('A', {'x': 5, 'y': 10})
map1.add_vertex('B', {'x': 20, 'y': 5})
map1.add_vertex('C', {'x': 50, 'y': 5})
map1.add_vertex('D', {'x': 60, 'y':25})
map1.add_vertex('E', {'x': 65, 'y':30})
map1.add_vertex('F', {'x': 80, 'y':30})
map1.add_vertex('G', {'x': 100, 'y':40})
map1.add_vertex('H', {'x': 135, 'y':100})
map1.add_vertex('I', {'x': 150, 'y':250})
map1.add_vertex('K', {'x': 180, 'y':250})
map1.add_vertex('L', {'x': 200, 'y':200})
map1.add_vertex('M', {'x': 250, 'y':250})
#Adding vertices to the map, with a unique identifier and location

vertices=map1.get_vertices() 
for i in range(len(vertices)):
    for o in range(len(vertices)): # Two loops are used, one for the first value, the second for the other respectively
            map1.add_edge(str(vertices[i]),str(vertices[o]),random.randint(5,100)) #Adds all the vertices to the current "main" vertex
    map1.remove_edge(str(vertices[i]),str(vertices[i])) #The second for loop ads duplicates, which this code removes before moving to the next iteration
#Adding edges (connections) between the vertices, by setting the starting and ending locations and the weight of the roads

print(map1.get_vertices())
print(map1.get_edges())
print(map1.get_edge_weight('F','E'))
print(map1.get_neighbors('A'))
print(map1.get_neighbors('K'))
print(map1.get_neighbors('F'))
print(map1.get_edge_weight('A','B'))
#Code to check if map creation was succesful