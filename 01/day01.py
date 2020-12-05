#!/usr/bin/env python3
## https://adventofcode.com/2020/day/1
import argparse
import sys
import time

SUM = 2020

def part_one(data, progress=False):
    for i in range(len(data)):
        for j in range(i+1, len(data[i+1:])):
            a = int(data[i])
            b = int(data[j])
            sum = a + b
            if progress:
                print(f'\ra {a:4} ({i:03}) | b {b:4} ({j:03}) = {sum}', end='\r')
                time.sleep(0.01)
            if sum == SUM:
                product = a * b 
                if progress: print()
                print(f'{a} * {b} = {product}')
                return product
            elif sum > SUM:
                break

def part_two(data, progress=False):
    for i in range(len(data)):
        for j in range(i+1, len(data[i+1:])):
            for k in range(i+j+1, len(data[i+j+1:])):
                a = data[i]
                b = data[j]
                c = data[k]
                sum = a + b + c
                if progress:
                    print(f'\ra {a:4} ({i:03}) | b {b:4} ({j:03}) | c {c:4} ({k:03}) = {sum}', end='\r')
                    time.sleep(0.01)
                if sum == SUM:
                    product = a * b * c
                    if progress: print()
                    print(f'{a} * {b} * {c} = {product}')
                    return product
                elif sum > SUM:
                    break

def sorted_data():
    with open('data', 'r') as f:
        return list(sorted(map(lambda x: int(x), f.readlines())))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--progress', action="store_true", help="show progress of calculation")
    args = parser.parse_args()
    
    data = sorted_data()
    part_one(data, args.progress)
    part_two(data, args.progress)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)
