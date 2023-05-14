from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    description="My Python package",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/Jameakelan/mypackage",
    install_requires=[
        'numpy',
    ],
)
