import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="query",
    version="0.1",
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
    packages=["upc_query"],
    include_package_data=True,
    install_requires=[
        "requests",
    ],
    entry_points={"console_scripts": ["upc_query=upc_query.__main__:main"]},
)