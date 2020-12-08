#!/usr/bin/env python3
## https://adventofcode.com/2020/day/6
from argparse import ArgumentParser
from functools import reduce
import os
import sys

def read():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'data'), 'r') as f:
        return f.read()

def split(word):
    return [c for c in word]

def part_one(data, verbose=False):
    groups = data.split('\n\n')
    res = [set(split("".join(group.splitlines()))) for group in groups]
    return reduce(lambda x,y: x+y, list(map(lambda x: len(x), res)))

def part_two(data, verbose=False):
    groups = list(map(lambda x: x.splitlines(), data.split('\n\n')))
    res = []
    for group in groups:
        if len(group) == 1:
            res.append(len(group[0]))
            continue
        d = dict()
        for sub in group:
            for c in split(sub): d[c] = 1 if c not in d else d[c]+1
        res.append(len(list(filter(lambda x: x == len(group), [d[c] for c in d]))))
    return reduce(lambda x,y: x+y, res)


def main():
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    data = read()
    print(f'(1) sum: {part_one(data, args.verbose)}')
    print(f'(2) sum: {part_two(data, args.verbose)}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)
