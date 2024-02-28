import os
import json
import tempfile


def interact(modules=[], mode=''):

    commands = '; '.join([f'from fxy.{module} import *' for module in modules])

    def is_tool(name):
        from shutil import which
        return which(name) is not None

    python = 'python3'
    if not is_tool(python):
        python = 'python'

    if mode:
        try:
            os.system(f'{python} -m IPython --no-banner -i -c "{commands}"')
        except Exception as e:
            print(e)
    else:
        try:
            os.system(f'{python} -i -c "{commands}"')
        except Exception as e:
            print(e)


def main():

    import argparse
    parser = argparse.ArgumentParser()

    # Mode
    parser.add_argument('-i', '--ipython', action='store_false', default=True, help='Disables IPython (plain Python).')

    # Module
    parser.add_argument('-c', '--calc', action='store_false', default=True, help='(MpMath)')
    parser.add_argument('-m', '--math', action='store_false', default=True, help='(SymPy)')
    parser.add_argument('-f', '--physics', action='store_false', default=True, help="(MpMath, NumPy, SciPy)")
    parser.add_argument('-s', '--statistics', action='store_false', default=True, help='(NumPy, Pandas, Scikit-Learn, StatsModels)')
    parser.add_argument('-p', '--plotting', action='store_false', default=True, help='(MatplotLib, Seaborn)')

    args = parser.parse_args()

    # Choice of environment and plotting
    mode = not(args.ipython)
    plot = not(args.plotting)
    os.environ['_FXY_MODE_'] = mode and 'true' or ''
    os.environ['_FXY_PLOT_'] = plot and 'true' or ''

    # Choice of library imports
    if not(args.calc):
        module = 'calc'
    elif not(args.math):
        module = 'math'
    elif not(args.physics):
        module = 'physics'
    elif not(args.statistics):
        module = 'stats'
    else:
        # Default is MPMath for "calculator"
        module = 'calc'

    interact([module], mode)


if __name__ == '__main__':
    main()
