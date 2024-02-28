# Numeric (Mathematical)
import os

_fxy_mode_ = os.environ.get('_FXY_MODE_')
_fxy_plot_ = os.environ.get('_FXY_PLOT_')

if _fxy_mode_:
    print('# CALC (MpMath)')

try:
    from mpmath import *
    if _fxy_mode_:
        print('from mpmath import *')
except:
    pass

if _fxy_plot_:
    from .plot import *
