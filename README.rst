fxy
===
.. |isympy| replace:: ``isympy``

Mnemonic imports and command ``fx`` with parameters to import libraries often used in research.

-  ``n`` (**N**\ UMERIC MATH)
-  ``s`` (**S**\ YMBOLIC MATH)
-  ``a`` (**A**\ CTUARIAL: STATISTICS & SCIENCE)
-  ``l`` (MACHINE **L**\ EARNING)
-  ``p`` (**P**\ LOTING).

.. image:: https://wiki.mindey.com/shared/screens/video-cover.png
   :target: https://wiki.mindey.com/shared/shots/b7aa5c4fa1aa174667b06de44-fxy.mp4


Introduction
------------

The people who come from tools like Maple, Matlab, Mathematica, and R, may find that Python requires a lot of mathematical imports just to start doing basic stuff. So, I tried to simplify it -- simply ``pip install fxy``, and you've got a command ``fx``, that starts Python with ``mpmath`` stuff pre-imported: so, you can start using Python like a calculator right away. If you need more, like symbolics, or statistics, or machine learning, -- these things are import-able with extra parameter, e.g., ``fx -s`` for |isympy|_ (shorter than typing `isympy`), or just by running import import shortcuts described below:

::

    >>> from fxy.n import * # Numeric: from mpmath import *
    >>> from fxy.s import * # Symbolic: import sympy; exec(sympy.interactive.session.preexec_source)
    >>> from fxy.a import * # Actuarial: numpy, np, pandas, pd, xarray, xr, scipy, sp, scipy.stats, st, statsmodels, sm, statsmodels.formula.api, smf
    >>> from fxy.l import * # Learning: sklearn, xgboost, xgb
    >>> from fxy.p import * # Plotting: matplotlib.pyplot, plt, matplotlib, seaborn, sns


Installation
------------

-  ``pip3 install fxy`` to get the import shortcuts.
-  ``pip3 install fxy[main]`` to install all libraries except ``xgboost``,
-  ``pip3 install fxy[all]`` (slow) to install all libraries for which the shortcuts exist.


Usage
-----
The package defines the `fx` command, if you just want Python with something, run:

-  ``$ fx -i[n|s|a|p|l]`` - plain Python (i: "IPython off")
-  ``$ fx -[n|s|a|p|l]`` - with IPython
-  ``$ fx -b[n|s|a|p|l]`` - with BPython and comments

Examples
========

In command line
---------------

Try various imports:

-  ``$ fx -b`` -- n(`mpmath <https://github.com/esamattis/slimux>`__) and plotting included.
-  ``$ fx -bs`` -- n(`mpmath <https://github.com/esamattis/slimux>`__) + s(`isympy <https://linux.die.net/man/1/isympy>`__) on top.
-  ``$ fx -bap``-- n(`mpmath <https://github.com/esamattis/slimux>`__) +  a(``numpy``, ``pandas``, ``xarray``, ``scipy``, ``statsmodels``), p(``matplotlib``, ``seaborn``)
-  ``$ fx -bsap`` -- n(`mpmath <https://github.com/esamattis/slimux>`__) + s(`isympy <https://linux.die.net/man/1/isympy>`__) + a(``numpy``, ``pandas``, ``xarray``, ``scipy``, ``statsmodels``), p(``matplotlib``, ``seaborn``)
-  ``$ fx -bsalp`` -- n(`mpmath <https://github.com/esamattis/slimux>`__) + s(`isympy <https://linux.die.net/man/1/isympy>`__) + a(``numpy``, ``pandas``, ``xarray``, ``scipy``, ``statsmodels``), l(``sklearn.* as sklearn``, ``xgboost as xgb``), p(``matplotlib``, ``seaborn``)

Just remove the ``b`` in the command to have them imported silently into `IPython`.

Within notebooks and Python code
--------------------------------

NB: This package does not assume versions of the imported packages, it just
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
    >>> neigh = sklearn.neighbors.KNeighborsClassifier(n_neighbors=3)
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


Suggestions
-----------

If you use some initialization commonly, we suggest adding ``~/.zshrc``, something like, for example:

::

   fxy() {
       fx -ap
   }

If you are using ``vim`` with ``tmux`` with `slimux <https://github.com/esamattis/slimux>`__, you may find it useful to something else to ``~/.zshrc``:

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


Conclusion
----------

This package may be useful for computing basic things, doing things to
emulate Python's capabilities in computational and symbolic mathematics
and statistics, so this package will introduce just convenient imports
so that one doesn't have to `configure Jupyter notebook
profile <https://mindey.com/blog/how_to_set_up_ipython_for_statistics_on_linux>`__,
to have those imports every time, and works well as an on-the-go
calculator.


I often collect convenient computations and functions in various fields,
like what `WolframAlpha <https://www.wolframalpha.com>`__
`does <https://wiki.mindey.com/shared/screens/Screenshot_2021-02-28_06-16-43.png>`__
cataloguing implementations of advanced computations to be reused.


.. _isympy:
    https://linux.die.net/man/1/isympy
