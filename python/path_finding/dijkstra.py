class Vertex():
    def __init__(self, x, y, value=1, previous=None, distance=float('inf'), neighbors=[]):
        self.x = x
        self.y = y
        self.value = value
        self.previous = previous
        self.distance = distance
        self.neighbors = neighbors

    def __str__(self):
        return "[{}, {}] (previous={}, distance={}, neighbors={})".format(self.x, self.y, self.previous, self.distance, self.neighbors)

def dijkstra(graph):
    vertices = [[ None for x in range(len(graph[y]))] for y in range(len(graph))]

    for y in range(len(graph)):
        for x in range(len(graph[y])):
            if graph[y][x] != 0:
                distance = float('inf')
                if x == 0 and y == 0:
                    distance = 0

                vertices[y][x] = Vertex(x=x, y=y, value=graph[y][x], distance=distance)

    for y in range(len(vertices)):
        for x in range(len(vertices[y])):
            if vertices[y][x]:
                neighbors = []
                moves = [
                    [-1, 0],
                    [1, 0],
                    [0, -1],
                    [0 , 1],
                ]
                for move in moves:
                    move_x = x + move[0]
                    move_y = y + move[1]
                    if move_y >= 0 and move_y < len(graph) and move_x >= 0 and move_x < len(graph[y]) and graph[move_y][move_x] != 0:
                        neighbors.append(vertices[move_y][move_x])
                vertices[y][x].neighbors = neighbors

    vertice_count = 0
    while len(list(filter(lambda v: v is not None, [x for y in vertices for x in y]))) > 0:
        minimum_distance = float('inf')
        for y in range(len(vertices)):
            for x in range(len(vertices[y])):
                if vertices[y][x] and vertices[y][x].distance < minimum_distance:
                    current_vertex = vertices[y][x]

        vertices[current_vertex.y][current_vertex.x] = None

        for neighbor in current_vertex.neighbors:
            distance = current_vertex.distance + 1
            if distance < neighbor.distance:
                neighbor.distance = distance
                neighbor.previous = current_vertex

            if neighbor.value == 9:
                return distance

    print('Failed!')

if __name__ == '__main__':
    graph = [
                [ 1, 1, 1, 1, ],
                [ 1, 0, 0, 0, ],
                [ 1, 1, 1, 1, ],
                [ 0, 0, 0, 1, ],
                [ 1, 1, 1, 9, ],
            ]

    return_value = dijkstra(graph)
    print('vlaue: {}'.format(return_value))
