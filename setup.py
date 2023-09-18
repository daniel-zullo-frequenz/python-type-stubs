"""Package setup"""
import os
from setuptools import setup

with open("README.md", "r") as f:
    read_me = f.read()

setup(
    name="python-type-stubs",
    version="0.0.1",
    url="https://github.com/daniel-zullo-frequenz/python-type-stubs",
    author="microsoft",
    description="A set of type stubs for popular Python packages.",
    license="MIT License",
    long_description=read_me,
    long_description_content_type="text/markdown",
    packages=find_packages(where="stubs"),
    package_dir={"": "stubs"},
    include_package_data=True,
    package_data={
        "networkx": ["*.pyi", "**/*.pyi", "**/**/*.pyi", "**/**/**/*.pyi"],
    },
    packages=[
        "networkx",
    ],
    python_requires=">=3.11",
    zip_safe=False,
)
