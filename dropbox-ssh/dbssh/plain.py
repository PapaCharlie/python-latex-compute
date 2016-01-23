from sympy import sympify, latex as to_latex
from utils import tex_to_plain, to_power_of10

def main(string, approx, latex, sci):
    string = tex_to_plain(string.strip())
    try:
        plain = sympify(string)
    except:
        plain = None
    if plain:
        if approx and sci:
            return to_latex(to_power_of10(plain.n(5))) if latex else to_power_of10(plain.n(5))
        if approx:
            return to_latex(plain.n(5)) if latex else plain.n(5)
        else:
            return to_latex(plain) if latex else plain