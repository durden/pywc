from setuptools import setup, find_packages

setup(
    name='pywc',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['Gooey>=1.0.1'],
    entry_points={
        'console_scripts': [
            'pywc = pywc.__main__:cli'
        ],
        'gui_scripts': [
            'pywcg = pywc.__main__:gui'
        ]
    },
)
