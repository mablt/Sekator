from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext
 
extensions = [
    Extension("AdapterTrimmer", ["AdapterTrimmer.pyx"]),
    Extension("QualityTrimmer", ["QualityTrimmer.pyx"]),
]
 
setup(
    cmdclass = {'build_ext':build_ext},
    ext_modules = cythonize(extensions),)