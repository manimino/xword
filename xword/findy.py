import os

from pathlib import Path

from hashbox import FrozenHashBox


def read_scrabble():
    fn = Path(os.getcwd()).parent / 'data' / 'scrabble.txt'
    ws = []
    with open(fn) as fh:
        for line in fh.readlines():
            ws.append(line.strip())
    return ws


if __name__ == '__main__':
    print(read_scrabble()[:100])
