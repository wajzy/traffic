import sys, CityMap as cm

class Car:
    def __init__(self, name, start_vertex, end_vertex):
        self.name = name
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.route = []
        self.distance = sys.maxsize

class NavigationSystem:
    def __init__(self, city_map):
        self.city_map = city_map
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def navigate(self):
        for car in self.cars:
            self.bellman_ford(car)

    def bellman_ford(self, car):
        distances = {vertex: sys.maxsize for vertex in self.city_map.get_vertices()}
        distances[car.start_vertex] = 0

        for _ in range(len(self.city_map.get_vertices()) - 1):
            for start_vertex, end_vertex in self.city_map.get_edges():
                weight = self.city_map.get_edge_weight(start_vertex, end_vertex)
                if distances[start_vertex] + weight < distances[end_vertex]:
                    distances[end_vertex] = distances[start_vertex] + weight

        car.route.append(car.start_vertex)
        current_vertex = car.start_vertex

        while current_vertex != car.end_vertex:
            neighbors = self.city_map.get_neighbors(current_vertex)
            min_distance = sys.maxsize
            next_vertex = None

            for neighbor in neighbors:
                if distances[neighbor] < min_distance:
                    min_distance = distances[neighbor]
                    next_vertex = neighbor

            if next_vertex:
                car.route.append(next_vertex)
                current_vertex = next_vertex
            else:
                break

        car.distance = distances[car.end_vertex]
        car.route.append(car.end_vertex)

    def print_routes(self):
        for car in self.cars:
            print(f"Car {car.name}: Start: {car.start_vertex}, Finish: {car.end_vertex}, Route: {car.route}, Distance: {car.distance}")


# Usage example
city_map = cm.CityMap()
city_map.add_vertex('A', {'x': 5, 'y': 10})
city_map.add_vertex('B', {'x': 20, 'y': 5})
city_map.add_vertex('C', {'x': 50, 'y': 5})
city_map.add_vertex('D', {'x': 60, 'y': 25})
city_map.add_vertex('E', {'x': 65, 'y': 30})
city_map.add_vertex('F', {'x': 80, 'y': 30})
city_map.add_vertex('G', {'x': 100, 'y': 40})
city_map.add_vertex('H', {'x': 135, 'y': 100})
city_map.add_vertex('I', {'x': 150, 'y': 250})
city_map.add_vertex('K', {'x': 180, 'y': 250})
city_map.add_vertex('L', {'x': 200, 'y': 200})
city_map.add_vertex('M', {'x': 250, 'y': 250})

city_map.add_edge('A', 'B', 20)
city_map.add_edge('A', 'C', 30)
city_map.add_edge('B', 'D', 40)
city_map.add_edge('C', 'D', 10)
city_map.add_edge('C', 'E', 20)
city_map.add_edge('D', 'F', 20)
city_map.add_edge('E', 'F', 10)
city_map.add_edge('E', 'G', 40)
city_map.add_edge('F', 'H', 60)
city_map.add_edge('G', 'H', 20)
city_map.add_edge('H', 'I', 150)
city_map.add_edge('I', 'K', 30)
city_map.add_edge('I', 'L', 80)
city_map.add_edge('K', 'L', 20)
city_map.add_edge('K', 'M', 50)
city_map.add_edge('L', 'M', 10)

nav_system = NavigationSystem(city_map)

car1 = Car('Car1', 'A', 'M')
car2 = Car('Car2', 'B', 'L')
car3 = Car('Car3', 'C', 'K')

nav_system.add_car(car1)
nav_system.add_car(car2)
nav_system.add_car(car3)

nav_system.navigate()
nav_system.print_routes()
