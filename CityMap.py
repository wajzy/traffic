# import tkinter as tk # unneeded imports; please remove them
# import heapq

class CityMap:
    def __init__(self):
        self.vertices = {}
        self.edges = {}
        self.vertex_data = {}
        self.edge_data = {}
        self.traffic_lights = set()

    def add_vertex(self, vertex, location=None):
        self.vertices[vertex] = location

    def remove_vertex(self, vertex):
        del self.vertices[vertex]
        # Remove any edges connected to the vertex
        self.edges = {k: v for k, v in self.edges.items() if vertex not in k}

    def add_edge(self, start_vertex, end_vertex, weight, additional_info=None):
        if start_vertex not in self.vertices or end_vertex not in self.vertices:
            raise ValueError("Start or end vertex does not exist in the map.")
        self.edges[(start_vertex, end_vertex)] = {'weight': weight, 'info': additional_info}

    def remove_edge(self, start_vertex, end_vertex):
        del self.edges[(start_vertex, end_vertex)]

    def get_vertices(self):
        return list(self.vertices.keys())

    def get_edges(self):
        return list(self.edges.keys())

    def get_vertex_location(self, vertex):
        return self.vertices[vertex]

    def add_traffic_light(self, vertex):
        self.traffic_lights.add(vertex)

    def remove_traffic_light(self, vertex):
        self.traffic_lights.discard(vertex)

    def has_traffic_light(self, vertex):
        return vertex in self.traffic_lights

    def get_edge_weight(self, start_vertex, end_vertex):
        return self.edges[(start_vertex, end_vertex)]['weight']

    def get_edge_info(self, start_vertex, end_vertex):
        return self.edges[(start_vertex, end_vertex)]['info']

    def get_neighbors(self, vertex):
        neighbors = []
        for (start_vertex, end_vertex) in self.edges.keys():
            if start_vertex == vertex:
                neighbors.append(end_vertex)
        return neighbors