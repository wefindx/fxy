# iSympy+
import os

_fxy_mode_ = os.environ.get('_FXY_MODE_')
_fxy_plot_ = os.environ.get('_FXY_PLOT_')

if _fxy_mode_:
    print('# MATH (SymPy)')

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

if _fxy_plot_:
    from .plot import *
