fxy
===
.. |isympy| replace:: ``isympy``

Mnemonic imports and command ``fx`` with parameters to import libraries often used in research.

-  ``c`` (**C**\ ALC)
-  ``m`` (**M**\ ATH)
-  ``f`` (**F**\ (PH)YSICS)
-  ``s`` (**S**\ TATISTICS)

.. image:: https://wiki.mindey.com/shared/screens/video-cover.png
   :target: https://wiki.mindey.com/shared/shots/b7aa5c4fa1aa174667b06de44-fxy.mp4


Introduction
------------

The people who come from tools like Maple, Matlab, Mathematica, and R, may find that Python requires a lot of mathematical imports just to start doing basic stuff. So, I tried to simplify it -- simply ``pip install fxy``, and you've got a command ``fx``, that starts Python with ``mpmath`` stuff pre-imported: so, you can start using Python like a calculator right away. If you need more, like symbolics, or statistics, or machine learning, -- these things are import-able with extra parameter, e.g., ``fx -m`` for |isympy|_ (shorter than typing `isympy`), or just by running import import shortcuts described below:


Installation
------------

-  ``pip install fxy`` to get the import shortcuts.

Usage
-----
The package defines the `fx` command, if you just want Python with something, run:

-  ``$ fx -[c|m|f|s]`` - plain Python (i: "IPython off")

Examples
========

In command line
---------------

-  ``$ fx -c`` -- imports useful for numeric math functions (mpmath)
-  ``$ fx -m`` -- imports useful for symbolic math functions (isympy)
-  ``$ fx -f`` -- imports usful for physics (scipy+)
-  ``$ fx -s`` -- imports usful for statistics (scikit-learn+)
-  ``$ fx -p`` -- imports usful for plotting (matplotlib+seaborn)

Additions:

-  ``$ fx`` -- calculator (equivalent to ``$fx -c``
-  ``$ fx -i`` -- calculator + IPython + explicit imports.
-  ``$ fx -ip`` -- calculator + plotting, with IPython.

E.g.,:

- ``$ fx -imp`` - math with IPython, and plotting imports
- ``$ fx -isp`` - stats with IPython, and plotting imports


Within notebooks and Python code
--------------------------------

NB: This package does not assume versions of the imported packages, it just
performs the basic imports, assuming that those namespaces within those
packages will exist for a long time to come, so it is
*dependencies-agnostic*.

::

    # Numeric (mpmath.*)
    >>> from fxy.calc import * (394 functions)
    >>> pi
    <pi: 3.14159~>

    # Symbolic (sympy.*)
    >>> from fxy.math import * (915 functions, and "isympy" imports)
    >>> f = x**4 - 4*x**3 + 4*x**2 - 2*x + 3
    >>> f.subs([(x, 2), (y, 4), (z, 0)])
    -1
    >>> plot(f)

    # Actuarial (np: numpy, pd: pandas, sm: statsmodels.api, sp: scipy, st: scipy.stats, smf: statsmodels.formula.api, statsmodels)
    >>> from fxy.stats import *
    >>> df = pandas.DataFrame({'x': numpy.arange(10), 'y': np.random.random(10)})
    >>> df.sum()
    x    45.000000
    y     4.196558
    dtype: float64

    # Learning (sklearn.* as sklearn)
    >>> X = [[0], [1], [2], [3]]
    >>> y = [0, 0, 1, 1]
    >>> neigh = sklearn.neighbors.KNeighborsClassifier(n_neighbors=3)
    >>> neigh.fit(X, y)
    >>> print(neigh.predict([[1.1]]))
    [0]
    >>> print(neigh.predict_proba([[0.9]]))
    [[0.66666667 0.33333333]]

    # Plotting (plt, matplotlib)
    >>> from fxy.plot import *
    >>> plt.plot([1, 2, 3, 4])
    >>> plt.ylabel('some numbers')
    >>> plt.show()
    <image>


Suggestions
-----------

If you use some initialization commonly, we suggest adding ``~/.zshrc``, something like, for example:

::

   alias f=". ~/.venv/bin/activate && fx -ic"

Or, pass params:

::

    function f() {
        . ~/.venv/bin/activate
        fx "$@"
    }


This way, running something like ``f`` makes a project folder and starts Python environment with packages ``fx -ap`` (IPython + Acturial + Plotting).


.. _isympy:
    https://linux.die.net/man/1/isympy
