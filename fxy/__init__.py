import os

def interact(module='n', mode=''):
    os.system(f'{mode}python -i -c "from fxy.{module} import *"')


def main():

    import argparse
    parser = argparse.ArgumentParser()

    # Mode
    parser.add_argument('-i', '--ipython', action='store_false', default=True, help='IPython.')

    # Module
    parser.add_argument('-n', '--numeric', action='store_false', default=True, help='Numeric.')
    parser.add_argument('-s', '--symbolic', action='store_false', default=True, help='Symbolic.')
    parser.add_argument('-a', '--actuarial', action='store_false', default=True, help='Actuarial.')
    parser.add_argument('-l', '--learning', action='store_false', default=True, help='Learning.')
    parser.add_argument('-p', '--plotting', action='store_false', default=True, help='Plotting.')

    args = parser.parse_args()

    i = not args.ipython

    n = not args.numeric
    s = not args.symbolic
    a = not args.actuarial
    l = not args.learning
    p = not args.plotting


    if i:
        mode = 'i'
    else:
        # Default is plain Python shell.
        mode = ''

    if p:
        module = 'p'
    elif n:
        module = 'n'
    elif s:
        module = 's'
    elif a:
        module = 'a'
    elif l:
        module = 'l'
    else:
        # Default is MPMath for "calculator"
        module = 'n'

    interact(module, mode)

if __name__ == '__main__':
    main()
