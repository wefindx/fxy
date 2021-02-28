# fxy
Just a convenience imports for scientific functions and packages for calculation.

`pip install fxy` to get the import shortcuts.
`pip install fxy[all]` to install all libraries for which the shortcuts exist.

## About
I'm lazy every time importing things I need for computing basic things, doing things to emulate Python's capabilities in computational and symbolic mathematics and statistics, so this package will introduce just convenient imports so that I don't have to set up my Jupyter lab every time, and works well as an on-the-go calculator.

This package does not assume versions of the imported packages, it just performs the basic imports, assuming that those namespaces within those packages will exist for a long time to come, so it is _dependencies-agnostic_.

I often use Python for powerful **math**, importing:

```
from mpmath import *
import matplotlib.pyplot as plt
```

I often use Python to do **calculus**, emulateing **[Maple](https://www.maplesoft.com)** and **[Mathematica](https://www.wolfram.com/mathematica/)**'s functionality:

```
import sympy
from sympy import symbols
x, y = symbols('x y')
```

I often use Python to do **statistics**, emulating **[base-R language](https://www.r-project.org)**, importing:

```
import numpy as np; import numpy
import pandas as pd; import pandas
import scipy.stats as st; import scipy
import statsmodels.api as sm; import statsmodels
import statsmodels.formula.api as smf
```
and [configuring Jupyter notebook profile](https://mindey.com/blog/how_to_set_up_ipython_for_statistics_on_linux), to have those imports...

I often use Python to emulate **[MATLAB](https://www.mathworks.com/products/matlab.html)**'s functionality:

```
import scipy
import scipy.optimize
import scipy.integrate
import scipy.interpolate
```

I often collect convenient computations and functions in various fields, like what **[WolframAlpha](https://www.wolframalpha.com)** [does](https://wiki.mindey.com/shared/screens/Screenshot_2021-02-28_06-16-43.png) cataloguing implementations of advanced computations to be reused.


## Usage

`from fxy.n import *`, if you need just `mpmath`.
`from fxy.np import *`, if you need just `mpmath` and `matplotlib`.
`from fxy.ns import *`, if you need just `mpmath` and `sympy`.
`from fxy.nsp import *`, if you need just `mpmath`, `sympy`, and `matplotlib`.
`from fxy.nsa import *`, if you need just `mpmath`, `sympy`, `numpy`, `pandas`, `scipy`, `statsmodels`.
`from fxy.nsap import *`, if you need just `mpmath`, `sympy`, `numpy`, `pandas`, `scipy`, `statsmodels`, and `matplotlib`.
`from fxy.nsal import *`, if you need just `mpmath`, `sympy`, `numpy`, `pandas`, `scipy`, `statsmodels` and `sklearn`.
`from fxy.nsalp import *`, if you need just `mpmath`, `sympy`, `numpy`, `pandas`, `scipy`, `statsmodels`, `sklearn`, and `matplotlib.

## Explanation

### Basic Math
`from fxy.n[umeric] import *` `<=>` `from mpmath import *; import mpmath`

### Basic Math & Calculus
`from fxy.ns[ymbolic] import *` `<=>` `from fxy.n import *` & `import sympy; exec(sympy.interactive.session.preexec_source)`

(Note: sympy is imported same as if it were run by [isympy](https://linux.die.net/man/1/isympy) command.)

### Basic Math & Statistics
`from fxy.nsa[ctuarial] import *` `<=>` `from fxy.ns import *` &
```
import numpy
import numpy as np
import pandas
import pandas as pd
import scipy
import scipy.stats as st
import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
```

### Basic Math & Statistics and Machine Learning
`from fxy.nsal[earning] import *` `<=>` `from fxy.nsa import *` & `import sklearn`


### Basic Math & Statistics, and Plotting
`from fxy.__p[lotting] import *` `<=>` `from fxy.__ import *` &
```
import matplotlib.pyplot as plt; import matplotlib
```
