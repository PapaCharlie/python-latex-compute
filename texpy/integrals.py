#!/usr/bin/python2

from sympy import Symbol, sympify, Integral, latex as to_latex#, symbols
import re

from utils import replace_frac, replace_exponents, replace_implicit_mult, string_to_int

# x, y, z = symbols("x y z")

def tex_integrals(string):
    string = replace_frac(string.strip())

    integ = "|".join((r'\int',r'\dint',r'\bigint'))

    d = "[{(]?-?\d[)}]?"
    op = re.match("^\W*("+integ+")(_({d})\^({d})|\^({d})_({d}))?(.*)(\W|\\,)*d(.)".format(d=d), string)
    if op:
        x = Symbol(op.group(9))
        body = op.group(7)
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
    op = re.match("^\W*integrate (.*)\W*(from ((\d) to (\d)))?", string)
    if op:
        op = op.groups()
        x = sympify(op[0]).free_symbols.pop()
        if op[1]:
            down, up = string_to_int(op[2]), string_to_int(op[3])
            return Integral(op[0],(x, down, up)).doit()
        else:
            return Integral(op[0],x).doit()

def main(string, approx, latex):
    tex = tex_integrals(string) or plain_integrals(string)
    if tex:
        if approx:
            return to_latex(tex.n(5)) if latex else tex.n(5)
        else:
            return to_latex(tex) if latex else tex