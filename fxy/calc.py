# Numeric (Mathematical)
import os

_fxy_mode_ = os.environ.get('_FXY_MODE_')
_fxy_plot_ = os.environ.get('_FXY_PLOT_')

if _fxy_mode_:
    print('# CALC (MpMath)')

try:
    from mpmath import *
    import eday
    if _fxy_mode_:
        print('from mpmath import *; import eday')
except:
    pass

if _fxy_plot_:
    from .plot import *

if __name__ == '__main__':
    import sys

    exec('from fxy.calc import *')

    if len(sys.argv) > 1:
        expression = sys.argv[1]
        try:
            result = eval(expression)
            print(result)
        except Exception as e:
            print(f"Error evaluating expression: {e}")
    else:
        print("Please provide a valid 'fxy' expression to evaluate.")
