fxy
===
.. |isympy| replace:: ``isympy``

Imports and command ``fxy`` with parameters to import libraries often used in research to emulate CAS software, or LAB software.

Introduction
------------

1. People coming from ``R``, love that you can start quickly using it as a CALCulator,
2. People coming from use of CAS tools like ``Maple``, ``Mathematica`` have ``isympy``, that is narrowly focused,
3. People coming from computing LAB languages ``Matlab`` and ``R`` may find that ``Python`` requires quite a few imports just to do equivalent computing in Python.

This package ``fxy`` is a shorthand to do the imports packages to approximate these domains (CALC, CAS, and LAB) you've got a command ``fxy``, that starts Python with needed packages pre-imported: so, you can start using Python like a calculator right away.

Installation
------------

-  ``pip install fxy`` to get the import shortcuts.

Use as a calculator
-------------------
``$ fxy``
(pass, ``-i`` for IPython)

Usage as imports
----------------

- ``from fxy.calc import *`` for quick CALC - basic ``mpmath`` calculator, and ``eday`` for time
- ``from fxy.cas import *`` for basic CAS software ("Symbolic") emulation
- ``from fxy.lab import *`` for LAB software ("Numeric") emulation
- ``from fxy.plot import *`` for plotting imports.

Usage as command
----------------
The package defines the `fxy` command, if you just want Python with something, run:

- ``$ fxy --calc`` starts Python with CALC imports (basic ``mpmath`` calculator)
- ``$ fxy --cas`` (or ``-x``) starts Python with CAS (Computer Algebra System) imports (to emulate Maple, Matematica,..)
- ``$ fxy --lab`` (or ``-y``) starts Python with LAB (Linear AlgeBra system) imports (to emulate MATLAB, R,...)
- ``$ fxy --plot`` (or ``-p``) for plotting imports

So, for example, if you want LAB imports with plotting and in IPython, then you'd:

- ``$ fxy -ip --lab``

You can also run the equivalent of `--calc` environment, that imports ``mpmath`` and ``eday``, like this:

``python -m fxy "pi**2"``

The following are usage examples.

CALC
----

::

    >>> from fxy.calc import *
    >>> pi
    <pi: 3.14159~>
    >>> mp.dps = 250
    >>> print(pi)

    >>> from fxy.plot import *
    >>> plt.plot([1, 2, 3, 4])
    >>> plt.ylabel('some numbers')
    >>> plt.show()

CAS
---

::

    >>> from fxy.cas import *
    >>> f = x**4 - 4*x**3 + 4*x**2 - 2*x + 3
    >>> f.subs([(x, 2), (y, 4), (z, 0)])
    -1
    >>> plot(f)
    >>> plot3d(x**2-y**2)

LAB
---

::

    >>> from fxy.lab import *
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

If you envy ``R`` users being able to start their 'calculator' with just one key, add something like the below to your ``~/.zshrc``:

::

    function f() {
        . ~/.venv/bin/activate
        fxy "$@"
    }
    function F() {
        f -ix # (your custom pre-configuration you often use)
    }


Aliasing ``fxy`` as ``f`` command as simplest generic, and commonly used specific as ``F`` command makes it possible to:

- Use ``f`` to start Python with just ``mpmath`` for fastest scientific calculations without ``IPython``.
- Use ``F`` to start Python with some specific other pre-configuration that you often use (e.g., ``f -ix`` emulates ``isympy``).


.. _isympy:
    https://linux.die.net/man/1/isympy
