import os

_fxy_mode_ = os.environ.get('_FXY_MODE_')
_fxy_plot_ = os.environ.get('_FXY_PLOT_')

if _fxy_mode_:
    print('# STATISTICS (NumPy, Pandas, Scikit-Learn, StatsModels)')

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
