from setuptools import setup, find_packages
import os

version = '2.0.4'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'bootstrap_submenu', 'test.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.bootstrap_submenu',
    version=version,
    description="fanstatic twitter bootstrap submenu.",
    long_description=long_description,
    classifiers=[],
    keywords='fanstatic twitter bootstrap submenu',
    author='Heberte Fernandes de Moraes',
    url='https://github.com/hmoraes/js.bootstrap-submenu',
    author_email='brebete@gmail.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery>=1.9.0',
        'js.bootstrap',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'bootstrap_submenu = js.bootstrap_submenu:library',
            ],
        },
    )
