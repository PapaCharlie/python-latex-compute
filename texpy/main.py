import integrals

def parse(string, **flags):
    print integrals.main(string, **flags) or "",
    print ""