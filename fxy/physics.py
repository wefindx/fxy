import os

_fxy_mode_ = os.environ.get('_FXY_MODE_')
_fxy_plot_ = os.environ.get('_FXY_PLOT_')

if _fxy_mode_:
    print('# PHYSICS (MpMath, NumPy, SciPy)')

try:
    import numpy
    import numpy as np
    if _fxy_mode_:
        print('import numpy; as np')
except:
    pass

try:
    from mpmath import *
    if _fxy_mode_:
        print('from mpmath import *')
except:
    pass

try:
    from . import _scipy as sci
    import scipy.stats as st
    if _fxy_mode_:
        print('import scipy; as sci')
        print('import scipy.stats as st')
except:
    pass

if _fxy_plot_:
    from .plot import *
