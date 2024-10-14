

# iSympy+
import os

_fxy_mode_ = os.environ.get('_FXY_MODE_')
_fxy_plot_ = os.environ.get('_FXY_PLOT_')

if _fxy_mode_:
    print('# CAS (SymPy, MpMath)')

try:
    import sympy
    import sympy as sp
    isympy = sympy.interactive.session.preexec_source
    extras = ["a, b, c, d = symbols('a b c d')",
              "from sympy.plotting import plot3d",
              "import sympy as sp"]
    lines = isympy.strip().split('\n')
    commands = '\n'.join(lines[:-1] + extras + lines[-1:])
    exec(commands)
    if _fxy_mode_:
        print(commands)
except:
    pass

try:
    from mpmath import mp
    import eday
    if _fxy_mode_:
        print('from mpmath import mp')
        print('import eday')
except:
    pass

if _fxy_plot_:
    from .plot import *

if __name__ == '__main__':
    import sys

    exec('from fxy.cas import *')

    if len(sys.argv) > 1:
        expression = sys.argv[1]
        try:
            result = eval(expression)
            print(result)
        except Exception as e:
            print(f"Error evaluating expression: {e}")
    else:
        print("Please provide a valid 'fxy' expression to evaluate.")
