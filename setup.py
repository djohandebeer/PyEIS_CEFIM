import setuptools
import re

# Read version from PyEIS/__init__.py
def get_version():
    with open("PyEIS/__init__.py") as f:
        content = f.read()
        version_match = re.search(r"__version__\s*=\s*['\"]([^'\"]+)['\"]", content)
        if version_match:
            return version_match.group(1)
    raise RuntimeError("Unable to find version string")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyEIS_CEFIM",
    version=get_version(),
    author="D. Johan De Beer",
    author_email="dirk.debeer@up.ac.za",
    description="A Python-based Electrochemical Impedance Spectroscopy simulator and analyzer (CEFIM branch)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djohandebeer/PyEIS_CEFIM",
    
    packages=['PyEIS'], 
    
    scripts=['bin/PyEIS_script.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pandas",
        "numpy",
        "scipy",
        "matplotlib",
        "mpmath",
        "lmfit",
        "seaborn"
    ],
)
