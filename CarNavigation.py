import heapq

class CarNavigation:
    def __init__(self, city_map):
        self.city_map = city_map
        self.start_vertex = None
        self.destination = None
        self.path = []
        self.current_position = None

    def set_initial_position(self, start_vertex):
        if start_vertex not in self.city_map.get_vertices():
            raise ValueError("Invalid start vertex.")
        self.start_vertex = start_vertex
        self.current_position = start_vertex

    def set_destination(self, destination):
        if destination not in self.city_map.get_vertices():
            raise ValueError("Invalid destination vertex.")
        self.destination = destination

    def dijkstra(self):
        if not self.start_vertex or not self.destination:
            raise ValueError("Start vertex or destination not set.")

        distances = {vertex: float('inf') for vertex in self.city_map.get_vertices()}
        distances[self.start_vertex] = 0

        previous_vertices = {vertex: None for vertex in self.city_map.get_vertices()}

        queue = [(0, self.start_vertex)]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_vertex == self.destination:
                break

            if current_distance > distances[current_vertex]:
                continue

            for neighbor in self.city_map.get_neighbors(current_vertex):
                weight = self.city_map.get_edge_weight(current_vertex, neighbor)
                if self.is_traffic_blocked(current_vertex, neighbor):
                    weight += 1  # Add a penalty for traffic
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(queue, (distance, neighbor))

        self.path = self._build_path(previous_vertices)

    def is_traffic_blocked(self, current_vertex, neighbor):
        current_location = self.city_map.get_vertex_location(current_vertex)
        neighbor_location = self.city_map.get_vertex_location(neighbor)
        distance = self.city_map.get_edge_weight(current_vertex, neighbor)
        buffer_distance = 4
        for vertex in self.city_map.get_vertices():
            if vertex == current_vertex or vertex == neighbor:
                continue
            vertex_location = self.city_map.get_vertex_location(vertex)
            if self._is_car_in_front(current_location, neighbor_location, vertex_location, distance + buffer_distance):
                return True
            if self._is_car_coming_from_right(current_location, neighbor_location, vertex_location, distance + buffer_distance):
                return True
        return False

    def _is_car_in_front(self, current_location, neighbor_location, vertex_location, distance_threshold):
        x1, y1 = current_location['x'], current_location['y']
        x2, y2 = neighbor_location['x'], neighbor_location['y']
        x3, y3 = vertex_location['x'], vertex_location['y']
        cross_product = (x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1)
        if cross_product == 0:
            if min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
                distance = abs(cross_product) / (x2 - x1)
                if distance <= distance_threshold:
                    return True
        return False

    def _is_car_coming_from_right(self, current_location, neighbor_location, vertex_location, distance_threshold):
        x1, y1 = current_location['x'], current_location['y']
        x2, y2 = neighbor_location['x'], neighbor_location['y']
        x3, y3 = vertex_location['x'], vertex_location['y']
        cross_product = (x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1)
        if cross_product > 0:
            distance = cross_product / (x2 - x1)
            if distance <= distance_threshold:
                return True
        return False

    def _build_path(self, previous_vertices):
        path = []
        vertex = self.destination
        while vertex is not None:
            path.insert(0, vertex)
            vertex = previous_vertices[vertex]
        return path

    def calculate_total_distance(self):
        total_distance = 0
        for i in range(len(self.path) - 1):
            start_vertex = self.path[i]
            end_vertex = self.path[i + 1]
            distance = self.city_map.get_edge_weight(start_vertex, end_vertex)
            total_distance += distance
        return total_distance

    def get_path(self):
        return self.path

    def get_current_position(self):
        return self.current_position

    def get_destination(self):
        return self.destination