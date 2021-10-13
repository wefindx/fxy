import os
import tempfile


def interact(modules=['n'], mode=''):
    command = 'from fxy.{} import *'

    annotation = lambda x: {
        'n': 'from mpmath import *',
        's': 'from __future__ import division; from sympy import *; x, y, z = symbols("xyz"); k, m, n = symbols("kmn", integer=True)',
        'a': 'numpy & np, pandas & pd, xarray & xr, scipy & sp, scipy.stats & st, statsmodels & sm, statsmodels.formula.api & smf',
        'l': 'from . import __sklearn__ as sklearn; xgboost & xgb',
        'p': 'matplotlib.pyplot & plt; matplotlib; seaborn & sns'
    }.get(x) or ''

    # BPython
    if mode == 'b':

        commands = '\n'.join([
            command.format(module) + ' # ' + str(annotation(module))
            for module in modules]) + '\n'

        with tempfile.NamedTemporaryFile(mode='wt', delete=False) as f:
            f.write(commands)
        os.system(f'{mode}python -i -q -p {f.name}')
        os.system(f'rm {f.name}')
    else:
        # Python & IPython
        commands = '; '.join([command.format(module) for module in modules])
        os.system(f'{mode}python3 -i -c "{commands}"')


def main():

    import argparse
    parser = argparse.ArgumentParser()

    # Mode
    parser.add_argument('-i', '--ipython', action='store_false', default=True, help='Disables IPython (plain Python).')
    parser.add_argument('-b', '--bpython', action='store_false', default=True, help='BPython.')

    # Module
    parser.add_argument('-n', '--numeric', action='store_false', default=True, help='Numeric.')
    parser.add_argument('-s', '--symbolic', action='store_false', default=True, help='Symbolic.')
    parser.add_argument('-a', '--actuarial', action='store_false', default=True, help='Actuarial.')
    parser.add_argument('-l', '--learning', action='store_false', default=True, help='Learning.')
    parser.add_argument('-p', '--plotting', action='store_false', default=True, help='Plotting.')

    args = parser.parse_args()

    i = not args.ipython # to disable IPython shell
    b = not args.bpython

    n = not args.numeric
    s = not args.symbolic
    a = not args.actuarial
    l = not args.learning
    p = not args.plotting


    if b:
        # BPython shell, cause more common.
        mode = 'b'
    elif i:
        # Plain Python shell (i.e., disable IPython shell).
        mode = ''
    else:
        # Default is IPython shell, cause more common.
        mode = 'i'

    # Default is MPMath for "calculator"
    modules = ['n']

    if s:
        modules.append('s')
    if a:
        modules.append('a')
    if l:
        modules.append('l')
    if p:
        modules.append('p')

    interact(modules, mode)

if __name__ == '__main__':
    main()
