#!/usr/bin/env python3
## https://adventofcode.com/2020/day/7
from argparse import ArgumentParser
import os
import re
import sys
import time

RE_GROUPS = re.compile(r'(\d{1,2})? ?(\w+ \w+) bags?')
SHINY_GOLD = 'shiny gold'

def read():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'data'), 'r') as f:
        return f.read()

def part_one(data, verbose=False):
    def filter_bags(all, sub):
        tmp = []
        for s in sub:
            tmp += list(map(lambda x: x[0], filter(lambda x: s in x[1:], all))) + list(sub)
        
        if len(set(tmp)) == len(set(sub)):
            return set(tmp)
        else:
            return filter_bags(all, set(tmp))

    groups = list(filter(lambda x: ('', 'no other') not in x, [RE_GROUPS.findall(d) for d in data.splitlines()]))
    bags = list(map(lambda x: [item for sublist in x for item in sublist][1::2], groups))
    return filter_bags(bags, [SHINY_GOLD]) - {SHINY_GOLD}


def part_two(data, verbose=False):
    return 'TODO'


def main():
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    data = read()
    print(f'(1) count: {len(part_one(data, args.verbose))}')
    print(f'(2) {part_two(data, args.verbose)}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)
