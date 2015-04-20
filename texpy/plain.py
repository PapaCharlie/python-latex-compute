from sympy import sympify, latex as to_latex
from utils import tex_to_plain

def main(string, approx, latex):
    string = tex_to_plain(string.strip())
    try:
        plain = sympify(string)
    except:
        plain = None
    if plain:
        if approx:
            return to_latex(plain.n(5)) if latex else plain.n(5)
        else:
            return to_latex(plain) if latex else plain