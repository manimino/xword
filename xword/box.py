import os

from flask import Flask
from functools import partial
from pathlib import Path

from filterbox import FrozenFilterBox, MissingAttribute

app = Flask(__name__)


def read_scrabble():
    fn = Path(os.getcwd()).parent / 'data' / 'all_words.txt'
    ws = []
    with open(fn) as fh:
        for line in fh.readlines():
            ws.append(line.strip())
    return ws


def char_at(pos, word):
    if pos >= len(word):
        raise MissingAttribute
    return word[pos]


def make_char_at_function(pos):
    p = partial(char_at, pos)
    p.__name__ = f'at_{pos}'
    return p


def make_box(words):
    max_word_len = max([len(w) for w in words])
    char_at = {pos: make_char_at_function(pos) for pos in range(max_word_len)}
    fb = FrozenFilterBox(words, char_at.values())
    return char_at, fb


@app.route("/")
def get():
    fb.find({char_at[10]: 'e'})


def main():
    words = read_scrabble()
    char_at, fb = make_box(words)



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    main()