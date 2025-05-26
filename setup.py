from setuptools import setup, find_packages

setup(
    name='cmf-sage',
    version='0.2.0',
    description='This project is to enable common metadata framework logging for waggle sensor plugins: https://github.com/waggle-sensor.',
    author='han.liu@hpe.com',
    packages=find_packages(),
    install_requires=[
        "cmflib",
        "pywaggle"

    ],
    python_requires='>=3.9',
)