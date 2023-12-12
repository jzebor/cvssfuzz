# CVSS Fuzz

## Introduction
CVSS Fuzz is a Python package designed for fuzzing implementations that utilize the Common Vulnerability Scoring System (CVSS). It aims to test and validate CVSS-related applications, ensuring robustness and reliability against a variety of inputs. Currently supports CVSS 4.0 and CVSS 3.1.

## Features
- Generation of fuzzed CVSS vectors.
- Customizable fuzzing strategies.
- Detailed logging and reporting.
- Import as module in your code or run from the command line.

## Installation
To install CVSS Fuzz, run the following command:

pip install cvzzfuzz

## Usage
To use CVSS Fuzz, import the package and use its provided functions. Below is a basic example:

```python
from cvssfuzz import Fuzzer

fuzzer = Fuzzer()
for vector in fuzzer.run():
    print(vector) 
    # your code here
```

## Configuration
CVSS Fuzz can be configured to suit various testing needs. Refer to the config.py file for configurable parameters.

## Contributing
Contributions to CVSS Fuzz are welcome! Please read the CONTRIBUTING.md file for guidelines on how to contribute.

## License
CVSS Fuzz is licensed under the MIT License. See the LICENSE file for more information.

## Security
Open a security issue and it will be dealt with promptly.

## Defects and Security Issues
For defects, feature requests and generally non-security related issues please open an issue.
For security issues, please open a security issue and it will be dealt with promptly.
