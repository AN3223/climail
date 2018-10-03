from setuptools import setup

setup(
    name='climail',
    version='0.1.0',
    description='A command line tool for checking email from the terminal',
    url='https://github.com/AN3223/climail',
    author='AN3223',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
    ],
    packages=["climail"],
    entry_points={
        'console_scripts': [
            'climail = climail.climail:main'
        ]
    },
    install_requires=[
        "fpbox",
        "imapclient"
    ]
)
