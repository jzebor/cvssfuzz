# CVSS Fuzz

## Introduction
CVSS Fuzz is a Python package designed for fuzzing implementations that utilize the Common Vulnerability Scoring System (CVSS). It aims to test and validate CVSS-related applications, ensuring robustness and reliability against a variety of inputs. Currently supports CVSS 4.0 and CVSS 3.1.

## Features
- Generation of fuzzed CVSS vectors.
- Customizable fuzzing strategies.
- Detailed logging and reporting.
- Import as module in your code or run from the command line.

## Installation
While under development, you can install CVSS Fuzz with this command:

pip install git+https://github.com/jzebor/cvzzfuzz


## Usage
### As a module in your test code
To use CVSS Fuzz, import the package and use its provided functions. Below is a basic example:

```python
from cvssfuzz import CVSSFuzz

fuzzer = CVSSFuzz()
config = {'iterations': 10000, "category": "base", "fuzzer": "random", "version": "4.0"}
for vector in fuzzer(config):
    print(vector) 
    # your code here
```

### As a stand-alone command line utility.
```
cvssfuzz --help

```


## Configuration
CVSS Fuzz can be configured to suit various testing needs. Refer to the config.py file for configurable parameters.
### Fuzzers
- Random: Random entries taken from valid values per metric. All output should be valid CVSS vector strings.
- Shuffle: Shuffles a randomly generated string.  All output should be valid CVSS vector strings, just in a shuffled order.
- Invalid: Insert an invalid metric value for a random metric.
- Insane: A random metric is chosen and substituted with an bad value (hex, url encoded, base64 encoded, etc)
- Missing: Drop a random metric from the vector.
- Duplicate: Duplicate a random metric from the vector.
- Lowecase: Lowercase a random metric from the vector.
- Missing Prefix: Drop the version prefix.

### Categories
#### CVSS 4.0
- Base: Just the base metrics (CVSS 4.0 OR CVSS 3.1)
- Threat: Base + Threat (CVSS 4.0)
- Environmental: Base + Environmental (CVSS 4.0)
- Supplemental: Base + Threat + Environmental + Supplemental (CVSS 4.0)
- All: Base + Threat + Environmental + Supplemental (CVSS 4.0)

#### CVSS 3.1
- Base: Just the base metrics (CVSS 3.1)
- Temporal: Base + Temporal
- Environmental: Base + Environmental
- All: Base + Temporal + Environmental

## Contributing
Contributions to CVSS Fuzz are welcome! Please read the CONTRIBUTING.md file for guidelines on how to contribute.

## License
CVSS Fuzz is licensed under the MIT License. See the LICENSE file for more information.

## Security
Open a security issue and it will be dealt with promptly.

## Defects and Security Issues
For defects, feature requests and generally non-security related issues please open an issue.
For security issues, please open a security issue and it will be dealt with promptly.
