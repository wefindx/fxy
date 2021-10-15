from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='fxy',
    version='0.4.6',
    description='Convenience imports and scientific functions.',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/mindey/fxy',
    author='Mindey',
    author_email='mindey@qq.com',
    license='UNLICENSE',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires=['mpmath', 'bpython', 'ipython', 'sympy'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
        'shells': ['bpython', 'ipython'],
        'main': ["bpython", "ipython", "sympy", "xarray", "scipy", "statsmodels", "sklearn", "matplotlib", "seaborn"],
        'all': ["bpython", "ipython"] + ["sympy", "xarray", "scipy", "statsmodels", "sklearn", "matplotlib", "seaborn"] + ["xgboost"]
    },
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'fx=fxy:main'
        ],
    }
)
