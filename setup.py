from setuptools import setup, find_packages

setup(
    name="cvssfuzz",
    version="0.1.0",
    license="BSD 2-Clause",
    description="A CVSS Fuzzing Package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jzebor/cvssfuzz',
    author="Jordan Zebor",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': ["cvssfuzz=cli:main"]
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Testing",
        "License :: BSD 2-Clause",
        "Programming Language :: Python :: 3.10",
    ],
)