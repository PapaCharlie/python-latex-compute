#!/usr/bin/python

from sympy import Symbol
from re import sub, findall, search
from math import log

def to_power_of10(num):
    return num

def replace_times(string):
    return string.replace(r"\times","*")

def replace_left_right(string):
    return string.replace(r"\left","").replace(r"\right","")

def replace_sqrt(string):
    sqrt = r'\sqrt' if r'\sqrt' in string else None
    if sqrt:
        s = string[string.find(sqrt)+len(sqrt):]
        o = 0
        for (i,c) in enumerate(s):
            if c == '{':
                o += 1
            elif c == "}":
                o -= 1
            if o == 0:
                num = s[1:i]
                break
        string = string[:string.find(sqrt)] + "sqrt(" + num + ")" + string[string.find(sqrt) + len(sqrt) + len(num) + 2:]
        return replace_sqrt(string)
    else:
        return string

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

def replace_exponents(string):
    i = string.find("^{")
    if i != -1:
        s = string[i+1:]
        o = 0
        for (k,c) in enumerate(s):
            if c == '{':
                o += 1
            elif c == "}":
                o -= 1
            if o == 0:
                exp = s[1:k]
                break
        string = string[:i+1] + "(" + exp + ")" + string[i+len(exp)+1 + 2:]
        return replace_exponents(string)
    else:
        return string


def fix_implicit_mult(string, vars):
    for x in vars:
        fr = search(r"[a-zA-Z0-9]{var}".format(var = x), string)
        if fr:
            string = string[:fr.end()-len(x)] + "*" + string[fr.end()-len(x):]
        fr = search(r"{var}[a-zA-Z0-9]".format(var = x), string)
        if fr:
            string = string[:fr.start()+len(x)] + "*"  + string[fr.start()+len(x):]
        return string
    return string


def string_to_int(s):
    if s:
        s = s.replace("(","").replace("{","").replace("}","").replace(")","")
        try:
            f = float(s)
            i = int(f)
            return i if i == f else f
        except ValueError:
            return Symbol(s)
        except:
            return None

def tex_to_plain(string):
    return replace_exponents(replace_frac(replace_times(replace_sqrt(replace_left_right(string)))))