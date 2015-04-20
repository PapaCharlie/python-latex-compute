#!/usr/bin/python2

from sympy import Symbol, sympify, Integral, latex as to_latex, symbols
import re
from difflib import get_close_matches

from utils import replace_frac, replace_exponents, string_to_int, fix_implicit_mult


def tex_integrals(string):
    integ = "|".join((r'\int',r'\dint',r'\bigint'))

    d = "[{(]?-?[a-zA-Z0-9][)}]?"
    op = re.match("^\W*("+integ+")(_({d})\^({d})|\^({d})_({d}))?(.*)(\W|\\,)*d(.)".format(d=d), string)
    if op:
        print op.groups()
        x = Symbol(op.group(9))
        body = fix_implicit_mult(op.group(7),[str(x)])
        inner = tex_integrals(body)
        if inner:
            body = inner.doit()
        if op.group(2):
            up = string_to_int(op.group(4)) or string_to_int(op.group(5))
            down = string_to_int(op.group(3)) or string_to_int(op.group(6))
            return Integral(body,(x,down, up)).doit()
        else:
            return Integral(body,x).doit()

def plain_integrals(string):
    x, y, z = symbols("x y z")
    string = string.strip()
    if get_close_matches(string[:string.find(" ")],['integrate','int']):
        string = string[string.find(" ")+1:]
        fr = re.search("\w{3,4}",string)
        if fr and get_close_matches(fr.group(), ['from']):
            body, (down, up) = string[:fr.start()], string[fr.end():].split("to" if "to" in string[fr.end():] else "..")
            if re.match("\W*\w+=\d+\W*",down):
                x,down = down.split('=')
                x = Symbol(x)
                down, up = string_to_int(down), string_to_int(up)
                body = fix_implicit_mult(body, map(str,[x]))
                return Integral(body,(x, down, up)).doit()
            else:
                down, up = string_to_int(down), string_to_int(up)
                body = fix_implicit_mult(body, map(str,[x,y,z]))
                x = sympify(body).free_symbols.pop()
                return Integral(body,(x, down, up)).doit()
        else:
            body = fix_implicit_mult(string, map(str,[x,y,z]))
            x = sympify(string).free_symbols.pop()
            return Integral(body,x).doit()

def main(string, approx, latex):
    tex = tex_integrals(string) or plain_integrals(string)
    if tex:
        if approx:
            return to_latex(tex.n(5)) if latex else tex.n(5)
        else:
            return to_latex(tex) if latex else tex