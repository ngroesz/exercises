"""Given a binary tree, count the number of visible nodes.
For some reason, recursion always tortures my brain."""

def print_tree(t):
    print(t.x)
    if t.l:
        print_tree(t.l)
    if t.r:
        print_tree(t.r)

class Tree(object):
    x = 0
    l = None
    r = None

    def __init__(self, t):
        if t is None:
            return
        self.x = t[0]
        if t[1]:
            self.l = Tree(t[1])
        if t[2]:
            self.r = Tree(t[2])


def count_visible_nodes(T, highest_value_in_path):
    if T is None:
        return 0

    my_value = 0

    if T.x >= highest_value_in_path:
        highest_value_in_path = T.x
        my_value = 1

    return my_value + count_visible_nodes(T.l, highest_value_in_path) + count_visible_nodes(T.r, highest_value_in_path)

def solution(T):
    if T is None:
        return 0
    else:
        return count_visible_nodes(T, T.x)


if __name__ == '__main__':
    t = Tree((5, (3, (20, None, None), (21, None, None)), (10, (1, None, None), None)))
    answer = solution(t)
    print('answer: {}'.format(answer))
    print_tree(t)
