from setuptools import find_packages, setup

setup(
    name='fxy',
    version='0.1.4',
    description='Convenience imports and scientific functions.',
    url='https://github.com/mindey/fxy',
    author='Mindey',
    author_email='mindey@qq.com',
    license='UNLICENSE',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires=[],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
        'all': ["mpmath", "sympy", "numpy", "pandas", "scipy", "statsmodels", "sklearn", "matplotlib"]
    },
    zip_safe=False
)
