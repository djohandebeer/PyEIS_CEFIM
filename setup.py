import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyEIS_CEFIM",
    version="0.1.0",
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
)
