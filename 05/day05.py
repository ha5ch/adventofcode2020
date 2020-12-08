#!/usr/bin/env python3
## https://adventofcode.com/2020/day/5
from argparse import ArgumentParser
import os
import sys

def read():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'data'), 'r') as f:
        return f.read()

def part_one(data, verbose=False):
    def divide(s, r):
        def is_lower(s):
            return s == 'F' or s == 'L'

        if len(s) == 1:
            return r[0] if is_lower(s) else r[1]

        if is_lower(s[0]):
            return divide(s[1:], r[:len(r)//2])
        else:
            return divide(s[1:], r[len(r)//2:])

    res = []
    for t in data.splitlines():
        row = divide(t[:len(t)-3], list(range(128)))
        col = divide(t[len(t)-3:], list(range(8)))
        id = row * 8 + col
        res.append((t, row, col, id))
        if verbose: print(f'{t} {row:3} {col:1} {id:4}')
    return sorted(res, key=lambda x: x[3])

def part_two(data, verbose=False):
    ids = list(map(lambda x: x[3], part_one(data, False)))
    for i in range(len(ids)-1):
        if ids[i] + 1 != ids[i+1]:
            return ids[i] + 1


def main():
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()
    
    data = read()
    print(f'highest id: {part_one(data, args.verbose)[-1][3]}')
    print(f'     my id: {part_two(data, args.verbose)}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)
