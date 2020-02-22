import os.path
from setuptools import setup, find_packages

#To-Do Finish the read me
HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="upc_query",
    version="0.2.6",
    description="Python wrapper for Querying Digit Eyes UPC Database",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/kc8/UPC_API",
    author="Kyle Cooper",
    author_email="kyle@cooperkyle.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(), #Use setup tools to discover packages, requires __init__.py in each pkg
    include_package_data=True,
    install_requires=[
        "requests",
    ],
)