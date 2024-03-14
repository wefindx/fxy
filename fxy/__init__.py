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
    parser.add_argument('-p', '--plotting', action='store_false', default=True, help='(MatplotLib, Seaborn)')

    # Module
    parser.add_argument('-f', '--calc', action='store_false', default=True, help='(MpMath)')
    parser.add_argument('-x', '--cas', action='store_false', default=True, help='CAS imports')
    parser.add_argument('-y', '--lab', action='store_false', default=True, help='LAB imports')

    args = parser.parse_args()

    # Choice of environment and plotting
    mode = not(args.ipython)
    plot = not(args.plotting)
    os.environ['_FXY_MODE_'] = mode and 'true' or ''
    os.environ['_FXY_PLOT_'] = plot and 'true' or ''
    # Default is MPMath for "calculator"
    module = 'calc'

    # Choice of library imports
    if not(args.calc):
        module = 'calc'
    if not(args.cas):
        module = 'cas'
    if not(args.lab):
        module = 'lab'

    interact([module], mode)


if __name__ == '__main__':
    main()
