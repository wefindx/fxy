fxy
===
.. |isympy| replace:: ``isympy``


Just a convenience imports for scientific functions and packages for calculation.

-  ``pip3 install fxy`` to get the import shortcuts.
-  ``pip3 install fxy[main]`` to install all libraries except ``xgboost``,
-  ``pip3 install fxy[all]`` (slow) to install all libraries for which the shortcuts exist.


If you are in existing environment of some kind, just do, to import:

-  ``from fxy.n import *``, if you need ``mpmath`` and plotting.
-  ``from fxy.s import *``, if you need |isympy|_ imports.
-  ``from fxy.a import *``, if you need ``numpy``, ``pandas``, ``xarray``,
   ``scipy``, ``statsmodels`` and ``matplotlib``, ``seaborn``.
-  ``from fxy.p import *``, if you need ``matplotlib`` and ``seaborn``.
-  ``from fxy.l import *``, if you need ``sklearn.* as sklearn`` and ``xgboost as xgb``.


.. image:: https://wiki.mindey.com/shared/screens/video-cover.png
   :target: https://wiki.mindey.com/shared/shots/5be13ae88af63324fbbd6f06c-set-of-imports.mp4

Usage
-----
The package defines the `fx` command, if you just want Python with something, run:

-  ``$ fx -[n|s|a|p|l]`` - with IPython
-  ``$ fx -b[n|s|a|p|l]`` - with BPython

Examples
========

-  ``fx`` -- IPython with n(`mpmath <https://github.com/esamattis/slimux>`__) and plotting included.
-  ``fx -s`` -- IPython with n(`mpmath <https://github.com/esamattis/slimux>`__) + s(`isympy <https://linux.die.net/man/1/isympy>`__) on top.
-  ``fx -bs``-- BPython with n(`mpmath <https://github.com/esamattis/slimux>`__) + s(`isympy <https://linux.die.net/man/1/isympy>`__) on top.
-  ``fx -ap``-- IPython with n9`mpmath <https://github.com/esamattis/slimux>`__) +  a(``numpy``, ``pandas``, ``xarray``, ``scipy``, ``statsmodels``), p(``matplotlib``, ``seaborn``)
-  ``fx -bap``-- BPython with n(`mpmath <https://github.com/esamattis/slimux>`__) +  a(``numpy``, ``pandas``, ``xarray``, ``scipy``, ``statsmodels``), p(``matplotlib``, ``seaborn``)
-  ``fx -sap`` -- IPython with n(`mpmath <https://github.com/esamattis/slimux>`__) + s(`isympy <https://linux.die.net/man/1/isympy>`__) + a(``numpy``, ``pandas``, ``xarray``, ``scipy``, ``statsmodels``), p(``matplotlib``, ``seaborn``)
-  ``fx -salp`` -- IPython with n(`mpmath <https://github.com/esamattis/slimux>`__) + s(`isympy <https://linux.die.net/man/1/isympy>`__) + a(``numpy``, ``pandas``, ``xarray``, ``scipy``, ``statsmodels``), l(``sklearn.* as sklearn``, ``xgboost as xgb``), p(``matplotlib``, ``seaborn``)


If you are using ``vim`` with ``tmux`` with `slimux <https://github.com/esamattis/slimux>`__, suggest adding ``~/.zshrc``:

::

   fxy() {
      if [ -n "$1" ]
        then
          mkdir -p "/home/mindey/Projects/Research/mindey/$1"
          cd "/home/mindey/Projects/Research/mindey/$1"
          touch main.py
          tmux new -s "$1-research" 'zsh' \; send-keys "vim main.py" Enter \; splitw -hd "python3 -mvenv .env && . .env/bin/activate; fx -bap"
        else
          echo "No project name selected."
      fi
   }

This way, running something like ``fxy project-name`` makes a project folder and starts Python environment with packages ``fx -bap`` (BPython + Acturial + Plotting).

Or simply use ``fxy`` as shortcut for some custom initialization that you often use, like:

::

   fxy() {
       fx -bnsalp
   }

This way, you created a command ``fxy`` that imports:

::

    >>> from fxy.n import * # Numeric: from mpmath import *
    >>> from fxy.s import * # Symbolic: import sympy; exec(sympy.interactive.session.preexec_source)
    >>> from fxy.a import * # Actuarial: numpy, np, pandas, pd, xarray, xr, scipy, sp, scipy.stats, st, statsmodels, sm, statsmodels.formula.api, smf
    >>> from fxy.l import * # Learning: sklearn, xgboost, xgb
    >>> from fxy.p import * # Plotting: matplotlib.pyplot, plt, matplotlib, seaborn, sns
    >>>


About
-----

This package may be useful for computing basic things, doing things to
emulate Python's capabilities in computational and symbolic mathematics
and statistics, so this package will introduce just convenient imports
so that one doesn't have to `configure Jupyter notebook
profile <https://mindey.com/blog/how_to_set_up_ipython_for_statistics_on_linux>`__,
to have those imports every time, and works well as an on-the-go
calculator.

This package does not assume versions of the imported packages, it just
performs the basic imports, assuming that those namespaces within those
packages will exist for a long time to come, so it is
*dependencies-agnostic*.

::

    # Numeric (mpmath.*)
    >>> from fxy.n import * (394 functions)
    >>> pi
    <pi: 3.14159~>

    # Symbolic (sympy.*)
    >>> from fxy.s import * (915 functions, and "isympy" imports)
    >>> f = x**4 - 4*x**3 + 4*x**2 - 2*x + 3
    >>> f.subs([(x, 2), (y, 4), (z, 0)])
    -1
    >>> plot(f)

    # Actuarial (np: numpy, pd: pandas, sm: statsmodels.api, sp: scipy, st: scipy.stats, smf: statsmodels.formula.api, statsmodels)
    >>> from fxy.a import *
    >>> df = pandas.DataFrame({'x': numpy.arange(10), 'y': np.random.random(10)})
    >>> df.sum()
    x    45.000000
    y     4.196558
    dtype: float64

    # Learning (sklearn.* as sklearn)
    >>> from fxy.l import *
    >>> X = [[0], [1], [2], [3]]
    >>> y = [0, 0, 1, 1]
    >>> neigh = skl.neighbors.KNeighborsClassifier(n_neighbors=3)
    >>> neigh.fit(X, y)
    >>> print(neigh.predict([[1.1]]))
    [0]
    >>> print(neigh.predict_proba([[0.9]]))
    [[0.66666667 0.33333333]]

    # Plotting (plt, matplotlib)
    >>> from fxy.p import *
    >>> plt.plot([1, 2, 3, 4])
    >>> plt.ylabel('some numbers')
    >>> plt.show()
    <image>

I often collect convenient computations and functions in various fields,
like what `WolframAlpha <https://www.wolframalpha.com>`__
`does <https://wiki.mindey.com/shared/screens/Screenshot_2021-02-28_06-16-43.png>`__
cataloguing implementations of advanced computations to be reused.


.. _isympy:
    https://linux.die.net/man/1/isympy
