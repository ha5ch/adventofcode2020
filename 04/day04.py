#!/usr/bin/env python3
## https://adventofcode.com/2020/day/4
from argparse import ArgumentParser
import os
import re
import sys


def read():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'data'), 'r') as f:
        return f.read()

def part_one(data):
    VALID_FULL = {'byr', 'hcl', 'cid', 'iyr', 'eyr', 'hgt', 'pid', 'ecl'}
    VALID_NPC  = {'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid'}
    
    def passport_splitter(passport):
        return dict(map(lambda x: x.split(':'), passport.split()))

    def passport_validater(passport):
        keys = set(passport_splitter(passport))
        return keys >= VALID_NPC and keys <= VALID_FULL
    
    return list(map(passport_splitter, filter(passport_validater, data.split('\n\n'))))

def part_two(data):
    RE_ECL = re.compile(r'amb|blu|brn|gry|grn|hzl|oth')
    RE_HCL = re.compile(r'#[0-9a-f]{6}')
    RE_HGT = re.compile(r'(\d{2,3})(in|cm)')
    RE_PID = re.compile(r'\d{9}')
    RE_YEAR = re.compile(r'\d{4}')

    def is_between(num, lower, higher):
        return num >= lower and num <= higher

    def is_year_between(val, lower, higher):
        return RE_YEAR.fullmatch(val) is not None and is_between(int(val), lower, higher)

    def check_hgt(hgt):
        res = RE_HGT.findall(hgt)
        if len(res) == 1 and len(res[0]) == 2:
            res = res[0]
            if res[1] == 'cm' and is_between(int(res[0]), 150, 193): return True
            if res[1] == 'in' and is_between(int(res[0]), 59, 76): return True
        return False

    def check_hcl(hcl):
        return RE_HCL.fullmatch(hcl) is not None

    def check_ecl(ecl):
        return RE_ECL.fullmatch(ecl) is not None

    def check_pid(pid):
        return RE_PID.fullmatch(pid) is not None

    def passport_validater(passport):
        return is_year_between(passport['byr'], 1920, 2002) \
           and is_year_between(passport['iyr'], 2010, 2020) \
           and is_year_between(passport['eyr'], 2020, 2030) \
           and check_hgt(passport['hgt']) \
           and check_hcl(passport['hcl']) \
           and check_ecl(passport['ecl']) \
           and check_pid(passport['pid'])

    return list(filter(passport_validater, part_one(data)))


def main():
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()

    data = read()

    p1 = part_one(data, args.verbose)
    if args.verbose: print(p1)
    print(f'{len(p1)} valid passports (step 1)')

    p2 = part_two(data, args.verbose)
    if args.verbose: print(p2)
    print(f'{len(p2)} valid passports (step 2)')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)
