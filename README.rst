fxy
===
.. |isympy| replace:: ``isympy``

Mnemonic imports and command ``fx`` with parameters to import libraries often used in research.

-  ``f`` (For CALC - Basic calculator)
-  ``x`` (For CAS software ("Numeric") emulation)
-  ``y`` (For LAB software ("Symbolic") emulation )


Introduction
------------

The people coming from use of CAS tools like ``Maple``, ``Mathematica`` or computing LAB languages ``Matlab`` and ``R`` may find that ``Python`` requires quite a few imports just to do equivalent computing.

This package ``fxy`` is a shorthand to do the imports packages to approximate these two domains (CAS, and LAB) you've got a command ``fx``, that starts Python with needed packages pre-imported: so, you can start using Python like a calculator right away.


Installation
------------

-  ``pip install fxy`` to get the import shortcuts.

Usage
-----
The package defines the `fx` command, if you just want Python with something, run:

-  ``$ fx -i[f|x|y]p`` - plain Python (i: "IPython on", p: "Plotting on")

Examples
========

In command line
---------------

-  ``$ fx`` -- calculator (equivalent to ``$fx -f``
-  ``$ fx -x``-- imports useful CAS functions (isympy+mpmath)
-  ``$ fx -y``-- imports useful LAB functions (Stats, ML, Physics)

Additions:

-  ``$ fx -i`` -- calculator + IPython + explicit imports.
-  ``$ fx -ip`` -- calculator + plotting, with IPython.

E.g.,:

- ``$ fx -ip`` - calc with IPython, and plotting imports
- ``$ fx -ipx`` - CAS with IPython, and plotting imports
- ``$ fx -ipy`` - LAB with IPython, and plotting imports


Within notebooks and Python code
--------------------------------

NB: This package does not assume versions of the imported packages, it just
performs the basic imports, assuming that those namespaces within those
packages will exist for a long time to come, so it is
*dependencies-agnostic*.

CALC
----

::

    >>> from fxy.calc import *
    >>> pi
    <pi: 3.14159~>

    >>> from fxy.plot import *
    >>> plt.plot([1, 2, 3, 4])
    >>> plt.ylabel('some numbers')
    >>> plt.show()

CAS
---

::

    >>> from fxy.CAS import *
    >>> f = x**4 - 4*x**3 + 4*x**2 - 2*x + 3
    >>> f.subs([(x, 2), (y, 4), (z, 0)])
    -1
    >>> plot(f)
    >>> plot3d(x**2-y**2)

LAB
---

::

    >>> from fxy.LAB import *
    >>> df = pandas.DataFrame({'x': numpy.arange(10), 'y': np.random.random(10)})
    >>> df.sum()
    x    45.000000
    y     4.196558
    dtype: float64

    >>> X = [[0], [1], [2], [3]]
    >>> y = [0, 0, 1, 1]
    >>> neigh = sklearn.neighbors.KNeighborsClassifier(n_neighbors=3)
    >>> neigh.fit(X, y)
    >>> print(neigh.predict([[1.1]]))
    [0]
    >>> print(neigh.predict_proba([[0.9]]))
    [[0.66666667 0.33333333]]


Suggestions
-----------

If you use some initialization commonly, we suggest adding ``~/.zshrc``, something like, for example:

::

   alias f=". ~/.venv/bin/activate && fx -if"

Or, pass params:

::

    function f() {
        . ~/.venv/bin/activate
        fx "$@"
    }


This way, running something like ``f`` makes a project folder and starts Python environment with import sets often used.


.. _isympy:
    https://linux.die.net/man/1/isympy
