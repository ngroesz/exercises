"""Given an airplane with 10 seats and two aisles
(seats in a 3-4-3 configuration) and some reserved
seats, figure out how many 3-person families can
sit together.
The problem stated "3-person families" but I coded this
solution to be more general.
Nothing really complicated about this code. The
two-dimensional array stores both seat spaces and aisle
"spaces", which makes the algorithm simple but is kinda weird,
I guess, conceptually.
"""


import re

seat_re = re.compile(r'^(\d+)([a-z]+)', re.I)
num_spaces_per_row = 12 # 10 seats + 2 aisle spaces
aisle_indices = (3, 8)

column_map = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 9,
    'J': 10,
    'K': 11
}

def mark_aisle_spaces(spaces):
    for row in spaces:
        for aisle in aisle_indices:
            row[aisle] = 'A'

def seat_string_to_array_indices(seat_string):
    result = seat_re.match(seat_string)
    if result:
        row_index = int(result.group(1)) - 1
        column_index = column_map[result.group(2)]
        return row_index, column_index
    else:
        raise ValueException('Unparseable seat: {}'.format(seat_string))

def reserve_seats(spaces, seat_string):
    for seat in seat_string.split():
        row_index, column_index = seat_string_to_array_indices(seat)
        spaces[row_index][column_index] = 'R'

def count_number_of_contiguous_open_seats(spaces, n):
    number_of_contiguous_open_seats = 0
    for row in spaces:
        open_seat_count = 0
        for seat in row:
            if seat is None:
                open_seat_count += 1
            else:
                open_seat_count = 0
            if open_seat_count == n:
                number_of_contiguous_open_seats += 1
                open_seat_count = 0

    return number_of_contiguous_open_seats

def solution(N, S):
    spaces = [[None] * num_spaces_per_row for i in range(N)]
    mark_aisle_spaces(spaces)
    reserve_seats(spaces, S)
    print_spaces(spaces)
    return count_number_of_contiguous_open_seats(spaces, 3)

def print_spaces(spaces):
    for row in spaces:
        print(row)

if __name__ == '__main__':
    s = solution(50, "1A 3C 2B 40G 5A")
    print("solution: {}".format(s))
