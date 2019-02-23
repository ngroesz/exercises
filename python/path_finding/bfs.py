# implementation of Breadth First Search, taken directly from wikipedia:
# https://en.wikipedia.org/wiki/Breadth-first_search

# this will find a path but not necessarily the shortest path

from collections import deque
from load_test_data import LoadTestData

def construct_path(end_vertex):
    current_vertex = end_vertex
    path_length = 0
    actions = deque()
    while current_vertex['previous_vertex'] is not None:
        actions.appendleft(current_vertex['action'])
        current_vertex = current_vertex['previous_vertex']
        path_length += 1

    for action in actions:
        print('move: {}'.format(action))

    return path_length

def breadth_first_search(graph):
    open_set = deque()
    closed_set = [[ False for x in range(len(graph[y]))] for y in range(len(graph))]
    open_set.append({'x': 0, 'y': 0, 'value': graph[0][0], 'previous_vertex': None, 'action': None})

    while len(open_set) > 0:
        subtree_root = open_set.popleft()

        if subtree_root['value'] == 9:
            return construct_path(subtree_root)

        offsets = [
            {'action': 'left',  'offset': [-1, 0] },
            {'action': 'right', 'offset': [1, 0]  },
            {'action': 'up',    'offset': [0, -1] },
            {'action': 'down',  'offset': [0, 1]  },
        ]

        for offset in offsets:
            y = subtree_root['y'] + offset['offset'][1]
            x = subtree_root['x'] + offset['offset'][0]
            if y >= 0 and y < len(graph) and x >= 0 and x < len(graph[y]) and graph[y][x] != 0:
                if closed_set[y][x]:
                    continue
                vertex = {'x': x, 'y': y, 'value': graph[y][x], 'previous_vertex': subtree_root, 'action': offset['action']}
                if vertex not in open_set:
                    open_set.append({'x': x, 'y': y, 'value': graph[y][x], 'previous_vertex': subtree_root, 'action': offset['action']})

        closed_set[subtree_root['y']][subtree_root['x']] = True


if __name__ == '__main__':
    test_data = LoadTestData('test_data_bfs.txt')

    counter = 0
    for problem in test_data.problems:
        counter += 1
        print('problem {}'.format(counter))
        answer = breadth_first_search(problem['graph'])
        assert(answer == problem['solution']), "{} != {}".format(answer, problem['solution'])
        print('passed!')
