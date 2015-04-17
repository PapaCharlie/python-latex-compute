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

# x, y, z = symbols("x y z")

ds = None
def tex_integrals(string):
    string = replace_frac(string.strip())

    integ = "|".join((r'\int',r'\dint',r'\bigint'))

    d = "[{(]?-?\d[)}]?"
    op = re.match("^\W*("+integ+")(_({d})\^({d})|\^({d})_({d}))?(.*)d(.)".format(d=d), string)
    global ds
    ds = op
    if op:
        print op.groups()
        x = Symbol(op.group(8))
        body = op.group(7)
        inner = tex_integrals(body)
        if inner:
            body = inner.doit()
        if op.group(2):
            up = sint(op.group(4)) or sint(op.group(5))
            down = sint(op.group(3)) or sint(op.group(6))
            return Integral(body,(x,down, up)).doit()
        else:
            return Integral(body,x)

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