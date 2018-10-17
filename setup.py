from setuptools import setup, find_packages

setup(
    name='pywc',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pywc = pywc.__main__:cli'
        ]
    },
)
