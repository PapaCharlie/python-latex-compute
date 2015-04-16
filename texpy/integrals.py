#!/usr/bin/python2

from sympy import sympify, symbols, Function, Integral, integrate, Symbol, latex as to_latex
import re


def sint(s):
    f = float(s)
    i = int(f)
    return i if i == f else f


def tex_integrals(string):
    integ = (r'\int',r'\dint',r'\bigint')

    op = re.match("^\W*("+"|".join(integ)+")(_(\d)\^(\d)|\^(\d)_(\d))?(.*)d(.)", string)
    if op:
        print op.groups()
        op = op.groups()
        x = Symbol(op[7])
        if op[1]:
            up = sint(op[3]) or sint(op[4])
            down = sint(op[2]) or sint(op[5])
            return Integral(op[6],(x,down, up)).doit()
        else:
            return Integral(op[6],x)

def plain_integrals(string):
    op = re.match("^\W*integrate (.*) from ((\d) to (\d))?", string)
    if op:
        print op.groups()
        op = op.groups()
        x = sympify(op[0]).free_symbols.pop()
        if op[1]:
            down, up = sint(op[2]), sint(op[3])
            return integrate(op[0],(x, down, up))
        else:
            return integrate(op[0],x)

def main(string, approx, latex):
    tex = tex_integrals(string) or plain_integrals(string)
    if tex:
        if approx:
            return to_latex(tex.n(5)) if latex else tex.n(5)
        else:
            return to_latex(tex) if latex else tex