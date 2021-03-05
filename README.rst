fxy
===
.. |isympy| replace:: ``isympy``


Just a convenience imports for scientific functions and packages for calculation.

-  ``pip install fxy`` to get the import shortcuts.
-  ``pip install fxy[main]`` to install all libraries except ``xgboost``,
-  ``pip install fxy[all]`` to install all libraries for which the shortcuts exist.

Usage
-----

If you are in existing environment of some kind, just do, to import:

-  ``from fxy.n import *``, if you need ``mpmath`` and plotting.
-  ``from fxy.s import *``, if you need |isympy|_ imports.
-  ``from fxy.a import *``, if you need ``numpy``, ``pandas``, ``xarray``,
   ``scipy``, ``statsmodels`` and ``matplotlib``, ``seaborn``.
-  ``from fxy.p import *``, if you need ``matplotlib`` and ``seaborn``.
-  ``from fxy.l import *``, if you need ``sklearn.* as sklearn`` and ``xgboost``.

If you are in command line, and just want Python with something, run:

-  ``$ fxy -[n|s|a|p|l]`` - to do with Python
-  ``$ fxy -i[n|s|a|p|l]`` - to do with IPython
-  ``$ fxy -b[n|s|a|p|l]`` - to do with BPython

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

    # Actuarial (np: numpy, pd: pandas, sm: statsmodels.api, st: scipy.stats, scipy, smf: statsmodels.formula.api, statsmodels)
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
