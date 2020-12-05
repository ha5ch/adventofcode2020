#!/usr/bin/env python3
## https://adventofcode.com/2020/day/3
from argparse import ArgumentParser
import re
import sys


def read():
    with open('data', 'r') as f:
        return f.read()

def part_one(data, printing=False, verbose=False):
    rows = data.splitlines()
    row_idx = 1
    if printing: print(f'{row_idx:03} {rows[0]}' if verbose else rows[0])
    pos = 3
    tree_cnt = 0
    for row in rows[1:]:
        row_idx += 1
        tree = row[pos] == '#'
        tree_cnt += 1 if tree else 0
        if printing:
            char = '\033[102mX\033[0m' if tree else '\033[101mO\033[0m'
            out = f'{row[:pos]}{char}{row[pos+1:]}'
            if verbose: out = f'{row_idx:03} {out} {char} {pos:2}'
            print(out)
        pos = (pos + 3) % len(row)
    return tree_cnt

def part_two(data, right, down, printing=False, verbose=False):
    rows = data.splitlines()
    if printing:
        for i in range(down):
            print(f'{i+1:03} {rows[i]}' if verbose else rows[i])
    pos = right % len(rows[0])
    tree_cnt = 0
    row_idx = down
    while row_idx < len(rows[down-1:]):
        row = rows[row_idx]
        tree = row[pos] == '#'
        tree_cnt += 1 if tree else 0
        if printing:
            char = '\033[102mX\033[0m' if tree else '\033[101mO\033[0m'
            out = f'{row[:pos]}{char}{row[pos+1:]}'
            if verbose: out = f'{row_idx+1:03} {out} {char} {pos:2}'
            print(out)
        pos = (pos + right) % len(row)
        row_idx += down
    return tree_cnt


def main():
    parser = ArgumentParser()
    parser.add_argument('part', nargs='?', type=str, default='one', 
    help='select part, possible: one  (part_one impl); two  (full part_two impl);')
    parser.add_argument('-p', '--print', help='print rows', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('-c', '--custom', help='set your own direction, e.g. r3d4 for right 3 down 4')

    args = parser.parse_args()

    data = read()
    if args.part == 'two':
        args.custom = 'r1d1,r3d1,r5d1,r7d1,r1d2'

    if args.custom is not None:
        slopes = re.findall(r'(r(\d{1,2})d(\d{1,2}))', args.custom)
        total = 1
        not_zero = 0
        for slope in slopes:
            result = part_two(data, int(slope[1]), int(slope[2]), args.print, args.verbose)
            print(f'{slope[0]}: {result}')
            not_zero += 1 if result > 0 else 0
            total *= result if result > 0 else 1
        if not_zero > 1:
            print('-----------------------')
            print(f'product of tree_counts: {total}') 
        sys.exit(0)

    if args.part == 'one':
        print(f'tree count: {part_one(data, args.print, args.verbose)}')
        sys.exit(0)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)
