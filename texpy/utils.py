#!/usr/bin/python

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
    return string

def replace_implicit_mult(string):
    return string

def string_to_int(s):
    if s:
        s = s.replace("(","").replace("{","").replace("}","").replace(")","")
        f = float(s)
        i = int(f)
        return i if i == f else f