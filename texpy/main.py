import integrals
import plain
from utils import tex_to_plain


def parse(string, **flags):
    print integrals.main(string, **flags) or "",
    print plain.main(string, **flags)