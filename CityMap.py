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

