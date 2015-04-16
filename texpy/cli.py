#!/usr/bin/python2

from argparse import ArgumentParser
from main import parse
import sys

escape_dict={'\a':r'\a',
           '\b':r'\b',
           '\c':r'\c',
           '\f':r'\f',
           '\n':r'\n',
           '\r':r'\r',
           '\t':r'\t',
           '\v':r'\v',
           '\'':r'\'',
           '\"':r'\"',
           '\0':r'\0',
           '\1':r'\1',
           '\2':r'\2',
           '\3':r'\3',
           '\4':r'\4',
           '\5':r'\5',
           '\6':r'\6',
           '\7':r'\7',
           '\8':r'\8',
           '\9':r'\9'}

def raw(text):
    """Returns a raw string representation of text"""
    new_string=''
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    return new_string

# k, m, n = symbols('k m n', integer=True)
# f, g, h = symbols('f g h', cls=Function)


def main():
    parser = ArgumentParser(description='Parse a LaTeX sting and attempt to compute a result.2')
    parser.add_argument('string', type=str, help='String to parse')
    parser.add_argument('-a', action='store_true', help='Return exact or approximate value')
    parser.add_argument('-l', action='store_true', help='Return as plaintext or LaTeX')
    args = parser.parse_args()
    parse(raw(args.string).strip(),**{"approx":args.a,"latex":args.l})

if __name__ == '__main__':
  sys.exit(main())