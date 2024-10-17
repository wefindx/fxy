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

def run_qtconsole(name):
    import subprocess
    import platform
    kernel = f'fxy_{name}'

    def kernel_exists(kernel_name):
        """Check if the kernel exists in state.json."""
        from appdirs import user_config_dir

        config_file = os.path.join(user_config_dir("fxy"), 'state.json')
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                variables = json.load(f)
                return kernel_name in variables
        return False

    if not kernel_exists(kernel):
        from .kernels import install_my_kernel_spec
        install_my_kernel_spec(
            kernel, [f'from fxy.{name} import *', 'from fxy.plot import *'])

    command = ['jupyter-qtconsole', '--kernel', kernel]

    try:
        if platform.system() == 'Windows':
            subprocess.run(command, shell=True)
        else:
            subprocess.run(command)
    except FileNotFoundError:
        print(f"jupyter-qtconsole or kernel '{kernel}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():

    import argparse
    parser = argparse.ArgumentParser()

    # Mode
    parser.add_argument('-i', '--ipython', action='store_false', default=True, help='Verbose imports, IPython mode.')
    parser.add_argument('-q', '--qt', action='store_false', default=True, help='Kernel imports, QTConsole mode.')

    # Module
    parser.add_argument('-f', '--calc', action='store_false', default=True, help='CALC imports')
    parser.add_argument('-x', '--cas', action='store_false', default=True, help='CAS imports')
    parser.add_argument('-y', '--lab', action='store_false', default=True, help='LAB imports')
    parser.add_argument('-p', '--plotting', action='store_false', default=True, help='(MatplotLib, Seaborn)')


    args = parser.parse_args()

    # If QTConsole is selected, run the appropriate kernel
    if not(args.qt):

        if not(args.calc):
            run_qtconsole('calc')
            return
        if not(args.cas):
            run_qtconsole('cas')
            return
        if not(args.lab):
            run_qtconsole('lab')
            return

        run_qtconsole('calc')
        return

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
