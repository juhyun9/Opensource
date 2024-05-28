from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

install_requires = [
    'textblob',
    ]



setup (
    name             = 'feeling', 
    packages=find_packages(where='src'),
    version          = '1.0.0',
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    install_requires = install_requires,
    author           = 'juhyun9, carol7378, yvonnekwak', 
    author_email     = 'juhyunkim999@gmail.com, caroll7378@gmail.com, yebonkwak915@gmail.com',
    description      = 'Desc'
)