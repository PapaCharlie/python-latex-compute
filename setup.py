from setuptools import setup
from texpy.__init__ import __version__ as VERSION

setup(
      name='texpy',
      version=VERSION,
      description='Execute simple math and TeX code',
      url='https://github.com/PapaCharlie/texpy',
      author='Paul Chesnais',
      author_email='paul.chesnais @ gmail',
      license='MIT',
      packages=['texpy'],
      package_dir={'texpy':'texpy'},
      entry_points={'console_scripts': ['texpy = texpy.cli:main',]},
      install_requires=['sympy>=0.7.4.1', ],
)