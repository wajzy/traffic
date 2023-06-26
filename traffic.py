import CityMap as cm

# Create a city map 
map = cm.CityMap()

# Vertices
map.add_vertex('A', location=(10, 20))
map.add_vertex('B', location=(30, 40))
map.add_vertex('C', location=(50, 60))

print(map.get_vertices())
print(map.get_vertex_location('A'))
#print(map.get_vertex_location('x')) # KeyError
if('B' in map.get_vertices()):
    print(map.get_vertex_location('B'))

print(map.has_traffic_light('A'))
map.add_traffic_light('A')
print(map.has_traffic_light('A'))
map.remove_traffic_light('A')
print(map.has_traffic_light('A'))
# We know nothing about the state of the lamp; what color it has? And in what direction?
map.add_traffic_light('x')
# No protection against adding a traffic lamp to a non-existing vertex

# Edges
map.add_edge('A', 'B', 5, 'shortest')
map.add_edge('B', 'C', 8)
map.add_edge('C', 'A', 10, 'longest')

print(map.get_edges())
print(map.get_edge_weight('A', 'B'))
print(map.get_edge_info('A', 'B'))
# set_edge_info() is missing; how do you want to store/update the location of cars along the edges?
print(map.get_neighbors('A'))

map.remove_vertex('A')
print(map.get_vertices())
print(map.get_edges())