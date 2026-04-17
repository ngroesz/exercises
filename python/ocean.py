""" Calculate the size of the largest "island" of 1s in a sea of 0s
"""

ocean = [
    [0, 0, 1, 1, 0, 0, ],
    [0, 0, 1, 1, 0, 0, ],
    [1, 1, 0, 0, 1, 1, ],
    [1, 1, 0, 0, 1, 1, ],
    [1, 1, 0, 0, 1, 1, ],
    [1, 1, 0, 0, 1, 1, ],
    [0, 0, 0, 0, 1, 1, ],
]

def swim(ocean):
    greatest_size = 0
    print('height: {}'.format(len(ocean)))
    print('width: {}'.format(len(ocean[0])))
    for y in range(len(ocean)):
        for x in range(len(ocean[y])):
            width = 0
            local_x = x
            greatest_height = 0
            while (local_x < len(ocean[y]) and ocean[y][local_x] == 1):
                width += 1
                local_y = y
                height = 0
                while(local_y < len(ocean) and ocean[local_y][x] == 1):
                    local_y += 1
                    height += 1
                    if height > greatest_height:
                        greatest_height = height
                local_x += 1
            if width * greatest_height > greatest_size:
                greatest_size = width * greatest_height

    return greatest_size


if __name__ == '__main__':
    result = swim(ocean)
    print("result = {}".format(result))

