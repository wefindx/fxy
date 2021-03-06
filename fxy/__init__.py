import os

def interact(modules=['n'], mode=''):
    command = 'from fxy.{} import *'

    # BPython
    if mode == 'b':
        commands = '\n'.join([command.format(module) for module in modules]) + '\n'
        path = os.path.normpath(os.path.join(__loader__.path, f'../__paste__/commands.txt'))
        with open(path, 'w') as f:
            f.write(commands)
        os.system(f'{mode}python -i -q -p {path}')
    else:
        # Python & IPython
        commands = '; '.join([command.format(module) for module in modules])
        os.system(f'{mode}python3 -i -c "{commands}"')


def main():

    import argparse
    parser = argparse.ArgumentParser()

    # Mode
    parser.add_argument('-i', '--ipython', action='store_false', default=True, help='IPython.')
    parser.add_argument('-b', '--bpython', action='store_false', default=True, help='BPython.')

    # Module
    parser.add_argument('-n', '--numeric', action='store_false', default=True, help='Numeric.')
    parser.add_argument('-s', '--symbolic', action='store_false', default=True, help='Symbolic.')
    parser.add_argument('-a', '--actuarial', action='store_false', default=True, help='Actuarial.')
    parser.add_argument('-l', '--learning', action='store_false', default=True, help='Learning.')
    parser.add_argument('-p', '--plotting', action='store_false', default=True, help='Plotting.')

    args = parser.parse_args()

    i = not args.ipython
    b = not args.bpython

    n = not args.numeric
    s = not args.symbolic
    a = not args.actuarial
    l = not args.learning
    p = not args.plotting


    if i:
        mode = 'i'
    else:
        # Default is plain BPython shell for faster loading +  providing educational info.
        mode = 'b'

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
