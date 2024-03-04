import os

_fxy_mode_ = os.environ.get('_FXY_MODE_')
_fxy_plot_ = os.environ.get('_FXY_PLOT_')

if _fxy_mode_:
    print('# LAB (MpMath, NumPy, Pandas, Xarray, SciPy, Scikit-Learn, StatsModels)')

try:
    from mpmath import *
    if _fxy_mode_:
        print('from mpmath import *')
except:
    pass

try:
    import sympy
    import sympy as sp
    if _fxy_mode_:
        print('import sympy; as sp')
except:
    pass

try:
    import numpy
    import numpy as np
    if _fxy_mode_:
        print('import numpy; as np')
except:
    pass

try:
    import pandas
    import pandas as pd
    if _fxy_mode_:
        print('import pandas; as pd')
except:
    pass

try:
    import xarray
    import xarray as xr
    if _fxy_mode_:
        print('import xarray; as xr')
except:
    pass

try:
    from . import _scipy as scipy
    from . import _scipy as sci
    import scipy.stats as st
    if _fxy_mode_:
        print('import scipy; as sci')
        print('import scipy.stats as st')
except:
    pass

try:
    from . import _sklearn as sklearn
    from . import _sklearn as skl
    if _fxy_mode_:
        print('import sklearn; as skl')
except:
    pass

try:
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    if _fxy_mode_:
        print('import statsmodels.api as sm; .formula.api as smf')
except:
    pass

if _fxy_plot_:
    from .plot import *
