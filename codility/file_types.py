"""
Classify files into types using their extensions. Also,
aggregate sizes by type.
This scored only 11% on Codility. One potential issue is
that I used the splitext function, which may not be tolerant of
multiple dots in the filename. A regex would have probably been
better.
"""


import re
import os

file_re = re.compile(r'^([^\s]+)\s(\d+)b$')

extension_by_type = {
    'music': ['.mp3', '.aac', '.flac', ],
    'image': ['.jpg', '.bmp', '.gif', ],
    'movie': ['.mp4', '.avi', '.mkv', ],
}

def file_type_from_name(file_name):
    filename, file_extension = os.path.splitext(file_name)
    for type in extension_by_type:
        if file_extension in extension_by_type[type]:
            return type
    return 'other'

def solution(S):
    sizes_by_type = {
        'music': 0,
        'images': 0,
        'movie': 0,
        'other': 0
    }
    for file_line in S.split("\n"):
        file_result = file_re.match(file_line)
        if file_result:
            type = file_type_from_name(file_result.group(1))
            sizes_by_type[type] += int(file_result.group(2))
        else:
            raise Exception('count not parse file line: {}'.format(file_line))

    return """music {}b
images {}b
movies {}b
other {}b""".format(sizes_by_type['music'], sizes_by_type['images'], sizes_by_type['movie'], sizes_by_type['other'])

if __name__ == '__main__':
    files = """my.song.mp3 11b
greatsong.flac 1000b
not3.txt 5b
video.mp4 200b
game.exe 100b
mov!e.mkv 10000b"""
    answer = solution(files)
    print('answer: {}'.format(answer))
