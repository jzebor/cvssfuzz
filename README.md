# CVSS Fuzz

## Introduction
CVSS Fuzz is a Python package designed for fuzzing implementations that utilize the Common Vulnerability Scoring System (CVSS). It aims to test and validate CVSS-related applications, ensuring robustness and reliability against a variety of inputs. Supports all versions of CVSS except version 1.

## Features
- Generation of fuzzed CVSS vectors.
- Customizable fuzzing strategies.
- Detailed logging and reporting. (WIP)
- Import as module in your code or run from the command line.

## Installation
While under development, you can install CVSS Fuzz with this command:

pip install git+https://github.com/jzebor/cvzzfuzz


## Usage
### As a module in your test code
To use CVSS Fuzz, import the package and use its provided functions.
```python
from cvssfuzz import CVSSFuzz
config = {'count': 10000, "category": "base", "fuzzer": "random", "version": "4.0"}
fuzzer = CVSSFuzz(config=config)
for vector in fuzzer.run():
    print(vector) 
    # your code here
```

### As a stand-alone command line utility
```
cvssfuzz --help
cvssfuzz --count 1 --version 4.0
cvssfuzz --count 100 --fuzzer insane --version 4.0 --category environmental
cvssfuzz --count 5 --version 2.0

```

## Configuration
CVSS Fuzz can be configured to suit various testing needs. Refer to the settings.py file for configurable parameters.

### Count
Count is just as it sounds. The option is for configuring the total of fuzzed vectors you want. Choosing a value of 0 causes it to run forever. CAUTION: Choosing a value of 0 can lead to out of memory conditions. Be mindful until I fix that part in the code.

### Fuzzers
Fuzzers can be configured to use one of the following options.

- random: Random entries taken from valid values per metric. All output should be valid CVSS vector strings.
- shuffle: Shuffles a randomly generated string.  All output should be valid CVSS vector strings, just in a shuffled order.
- invalid: Insert an invalid metric value for a random metric.
- insane: A random metric is chosen and substituted with an bad value (hex, url encoded, base64 encoded, etc)
- duplicate: Duplicate a random metric from the vector.
- lowercase: Lowercase a random metric from the vector.
- missing: Drop a random metric from the vector.
- missing_prefix: Drop the version prefix from the vector.
- missing_metric_key: Drop a random metric _key_ from the vector.
- missing_metric_value: Drop a random metric _value_ from the vector.

### Versions
Versions dictate the version to use for fuzzing. Currently CVSS 4.0, CVSS 3.1, CVSS 3.0, & CVSS 2.0 are supported.

### Categories
Categories are how you can define which specific metric groups to fuzz.

#### CVSS 4.0
- base: Just the base metrics
- threat: Base + Threat
- environmental: Base + Environmental
- supplemental: Base + Threat + Environmental + Supplemental
- all: Base + Threat + Environmental + Supplemental

#### CVSS 3.1
- base: Just the base metrics
- temporal: Base + Temporal
- environmental: Base + Environmental
- all: Base + Temporal + Environmental

#### CVSS 2.0
- base: Just the base metrics
- temporal: Base + Temporal
- environmental: Base + Environmental
- all: Base + Temporal + Environmental

## Contributing
Contributions to CVSS Fuzz are welcome!

## License
CVSS Fuzz is licensed under the BSD 2-Clause License. See the LICENSE file for more information.

## Defects and Security Issues
For defects, feature requests and generally non-security related issues please open an issue.
For security issues, please see SECURITY.md 
