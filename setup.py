from setuptools import setup
from distutils.sysconfig import get_python_lib

version = "1.0.0a1"

SITE_PACKAGES_PATH = get_python_lib()

setup(
    name="pyxl4",
    version=version,
    packages=["pyxl", "pyxl.codec", "pyxl.scripts"],
    url="https://github.com/pyxl4/pyxl4",
    description="Extend Python syntax with HTML.",
    maintainer="Adam Serafini",
    maintainer_email="adam@adamserafini.com",
    data_files=[(SITE_PACKAGES_PATH, ['pyxl.pth'])]
)
