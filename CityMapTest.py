# Create a city map 
map = CityMap()

# Vertices
map.add_vertex('A', location=(10, 20))
map.add_vertex('B', location=(30, 40))
map.add_vertex('C', location=(50, 60))

# Edges
map.add_edge('A', 'B', 5)
map.add_edge('B', 'C', 8)
map.add_edge('C', 'A', 10)

# Set additional information for vertices
map.set_vertex_info('A', 'population', 10000)
map.set_vertex_info('B', 'population', 20000)
map.set_vertex_info('C', 'population', 15000)

# Set geographical location for vertices
map.set_vertex_location('A', (10, 20))
map.set_vertex_location('B', (30, 40))
map.set_vertex_location('C', (50, 60))

# Current vertices and edges
print("Vertices:", map.get_vertices())
print("Edges:", map.get_edges())

# Edge weight
print("Edge weight between A and B:", map.get_edge_weight('A', 'B'))

# Additional information of vertices
print("Info of A:", map.get_vertex_info('A'))

# Geographical location of vertices
print("Location of A:", map.get_vertex_location('A'))
