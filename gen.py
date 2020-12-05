#!/usr/bin/env python3
from argparse import ArgumentParser
import os
import sys


def eprint(t: str) -> None:
    print(t, file=sys.stderr)

def py_template(day: int) -> str:
    return f"""#!/usr/bin/env python3
## https://adventofcode.com/2020/day/{day}
from argparse import ArgumentParser
import os
import sys

def read():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'data'), 'r') as f:
        return f.read()

def part_one(data):
    pass

def part_two(data):
    pass


def main():
    parser = ArgumentParser()
    # add arguments here ...

    args = parser.parse_args()

    data = read()
    
    part_one(data)
    part_two(data)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(2)
"""

def md_template(day: int) -> str:
    return f"""# [Day {day}](https://adventofcode.com/2020/day/{day})

* [Solution](./day0{day}.py)
* [Data](./data)

<!-- ADD CHALLENGE DESCRIPTION HERE -->
"""

def create_dir(day: int) -> None:
    os.mkdir(f'{day:02}')

def create_files(day: int) -> None:
    with open(f'{day:02}/day{day:02}.py', 'w') as f:
        f.write(py_template(day))
    with open(f'{day:02}/README.md', 'w') as f:
        f.write(md_template(day))
    with open(f'{day:02}/data', 'w') as f:
        pass


def main():
    parser = ArgumentParser()
    parser.add_argument('day', help="day of challenge", type=int)
    args = parser.parse_args()

    if args.day < 1 or args.day > 24:
        raise Exception(f'invalid day ({args.day}), has to be between 1 and 24!')

    create_dir(args.day)
    create_files(args.day)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
    except Exception as e:
        eprint(e)
        sys.exit(2)
