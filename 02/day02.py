#!/usr/bin/env python3
## https://adventofcode.com/2020/day/2
import argparse
import re
import sys

def data():
    with open('data', 'r') as f:
        return f.read()

def count(c, s):
    return len(list(filter(lambda x: x == c, s)))

def split(rng):
    return list(map(lambda x: int(x), rng.split('-')))

def create_part(p):
    """
    min, max, character, password
    """
    s = split(p[0])
    return s[0], s[1], p[1], p[2]

def part_one(parts, pv=False):
    valid = []
    for part in parts:
        f, t, c, pw = part
        cnt = count(c, pw)
        if cnt >= f and cnt <= t:
            if pv: print(f"{f} - {t} ({c}) [{pw}]")
            valid.append(part)

    return valid

def part_two(parts, pv=False):
    valid = []
    for part in parts:
        f, t, c, pw = part
        if ( (pw[f-1] == c and pw[t-1] != c) 
          or (pw[f-1] != c and pw[t-1] == c) ):
           if pv: print(f"{f} - {t} ({c}) [{pw}]") 
           valid.append(part)

    return valid


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action="store_true", default=False)
    args = parser.parse_args()

    parts = list(map(create_part, re.findall(r'(\d{1,2}\-\d{1,2}) (\w{1}): (\w+)', data(), re.M)))

    print(f"count of valids (1): {len(part_one(parts, args.verbose))}")
    print(f"count of valids (2): {len(part_two(parts, args.verbose))}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)
