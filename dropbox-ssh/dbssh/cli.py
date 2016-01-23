#!/usr/bin/python2

from argparse import ArgumentParser, ArgumentTypeError
from main import parse
import sys

def main():
    parser = ArgumentParser(description='Parse a LaTeX sting and attempt to compute a result.')
    parser.add_argument('-a', action='store_true', help='Return exact or approximate value')
    parser.add_argument('-s', action='store_true', help='Return as approximate to nearest power of 10')
    parser.add_argument('-l', action='store_true', help='Return as plaintext or LaTeX')
    parser.add_argument('string', type=str, help='String to parse', nargs='+')
    args = parser.parse_args()
    if args.s and not args.a:
        raise ArgumentTypeError("-a must be enabled for -s")
    parse(raw(" ".join(args.string)).strip(),**{"approx":args.a,"latex":args.l, "sci":args.s})

if __name__ == '__main__':
    sys.exit(main())
