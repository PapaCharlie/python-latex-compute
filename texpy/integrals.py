#!/usr/bin/python2

from sympy import sympify, symbols, Function, Integral, integrate, Symbol, latex as to_latex
import re


def sint(s):
    if s:
        s = s.replace("(","").replace("{","").replace("}","").replace(")","")
        f = float(s)
        i = int(f)
        return i if i == f else f

def replace_frac(string):
    frac = r'\dfrac' if r'\dfrac' in string else (r'\frac' if r'\frac' in string else None)
    if frac:
        s = string[string.find(frac)+len(frac):]
        o = 0
        for (i,c) in enumerate(s):
            if c == '{':
                o += 1
            elif c == "}":
                o -= 1
            if o == 0:
                num = s[1:i]
                break
        s = s[len(num)+2:]
        for (i,c) in enumerate(s):
            if c == '{':
                o += 1
            elif c == "}":
                o -= 1
            if o == 0:
                denum = s[1:i]
                break
        string = string[:string.find(frac)] + "(" + num + ")/("+ denum + ")" + string[string.find(frac) + len(frac) + len(num) + 2 + len(denum) + 2:]
        return replace_frac(string)
    else:
        return string


def tex_integrals(string):
    string = replace_frac(string)

    integ = "|".join((r'\int',r'\dint',r'\bigint'))

    d = "[{(]?-?\d[)}]?"
    op = re.match("^\W*("+integ+")(_({d})\^({d})|\^({d})_({d}))?(.*)d(.)".format(d=d), string)

    if op:
        x = Symbol(op.group(8))
        if op.group(2):
            up = sint(op.group(4)) or sint(op.group(5))
            down = sint(op.group(3)) or sint(op.group(6))
            return Integral(op.group(7),(x,down, up)).doit()
        else:
            return Integral(op.group(7),x)

def plain_integrals(string):
    op = re.match("^\W*integrate (.*) from ((\d) to (\d))?", string)
    if op:
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