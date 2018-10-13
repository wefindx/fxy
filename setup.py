from setuptools import find_packages, setup

setup(
    name='fxy',
    version='0.1.1',
    description='Scientific functions.',
    url='https://github.com/mindey/fxy',
    author='Mindey',
    author_email='mindey@qq.com',
    license='UNLICENSE',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires=["sympy", "scipy"],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    zip_safe=False
)
