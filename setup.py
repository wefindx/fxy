from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='fxy',
    version='0.5.7',
    description='Convenience imports and scientific functions.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/mindey/fxy',
    author='Mindey',
    author_email='mindey@mindey.com',
    license='UNLICENSE',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires=['mpmath', 'ipython', 'sympy', 'xarray', 'matplotlib', 'scikit-learn', 'scipy', 'statsmodels', 'seaborn', 'PyQt5', 'windows-curses >= 2.2.0 ; platform_system=="Windows"'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'fx=fxy:main'
        ],
    }
)
