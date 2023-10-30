from setuptools import setup, find_packages

setup(
    name="opendata",
    author="Giancarlo Rizzo",
    version="0.0.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pytest", 
        "pytest-cov",
        "jinja2<3.1.0",
        "pretty_errors",
        "pandas",
        ]
)