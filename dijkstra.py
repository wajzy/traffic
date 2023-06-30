import random
import time
import CityMap as cm
import CarNavigation as cn

# Create an instance of CityMap
map1 = cm.CityMap()

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
vertices = map1.get_vertices()
for i in range(len(vertices)):
    for o in range(len(vertices)):
        map1.add_edge(str(vertices[i]), str(vertices[o]), random.randint(5, 100))
    map1.remove_edge(str(vertices[i]), str(vertices[i]))

# Print vertices and edges for verification
print("Vertices:", map1.get_vertices())
print("Edges:", map1.get_edges())
print(map1.get_vertices())
print(map1.get_edges())
print(map1.get_edge_weight('F','E'))
print(map1.get_neighbors('A'))
print(map1.get_neighbors('K'))
print(map1.get_neighbors('F'))
print(map1.get_edge_weight('A','B'))

car_nav_1 = cn.CarNavigation(map1)
car_nav_1.set_initial_position('A')
car_nav_1.set_destination('H')
car_nav_1.dijkstra()

car_nav_2 = cn.CarNavigation(map1)
car_nav_2.set_initial_position('B')
car_nav_2.set_destination('L')
car_nav_2.dijkstra()

car_nav_3 = cn.CarNavigation(map1)
car_nav_3.set_initial_position('E')
car_nav_3.set_destination('M')
car_nav_3.dijkstra()

# Simulate movement of cars
cars = {
    "Car 1": {"car_nav": car_nav_1, "start_position": 'A', "waiting_attempts": 0},
    "Car 2": {"car_nav": car_nav_2, "start_position": 'B', "waiting_attempts": 0},
    "Car 3": {"car_nav": car_nav_3, "start_position": 'E', "waiting_attempts": 0}
}
current_positions = {car_name: {"current_position": car["car_nav"].get_current_position(), "start_position": car["start_position"]}
                     for car_name, car in cars.items()}

while any(car["car_nav"].get_current_position() != car["car_nav"].get_destination() for car in cars.values()):
    for car_name, car in cars.items():
        current_position = car["car_nav"].get_current_position()
        if current_position != car["car_nav"].get_destination():
            next_position = car["car_nav"].get_path()[car["car_nav"].get_path().index(current_position) + 1]
            # Check if the next position intersects with any other car's current position,
            # excluding the cars that have already reached their destinations
            intersection = any(next_position == position["current_position"] for name, position in current_positions.items()
                               if name != car_name and position["current_position"] != car["car_nav"].get_destination())
            if intersection:
                car["waiting_attempts"] += 1
                if car["waiting_attempts"] > 3:  # Threshold for number of waiting attempts
                    print(f"{car_name} is blocked. Waiting attempts exceeded the threshold.")
                    continue
                print(f"{car_name} is waiting for another car to move.")
                continue
            car["waiting_attempts"] = 0  # Reset waiting attempts
            # Update the current position of the car
            current_positions[car_name]["current_position"] = next_position
            car["car_nav"].current_position = next_position
            print(f"{car_name} - Start Position: {car['start_position']}, Current Position: {current_position} --> Next Position: {next_position}")
            time.sleep(1)  # Sleep for 1 second to simulate movement between vertices

        if car["car_nav"].get_current_position() == car["car_nav"].get_destination():
            print(f"{car_name} has reached its destination.")

    print()

for car_name, car in cars.items():
    car_nav = car["car_nav"]
    start_position = car["start_position"]
    print(f"{car_name} - Start Position: {start_position}")
    print(f"{car_name} Path: {car_nav.get_path()}")
    print(f"{car_name} Total Distance: {car_nav.calculate_total_distance()}")
    print()

print("All cars have reached their destinations.")