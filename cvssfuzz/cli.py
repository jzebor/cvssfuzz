import argparse
import sys
import logging

from cvssfuzz import CVSSFuzz

def main():
    default_settings = {"count": 5, "fuzzer": "random", "category": "base", "version": "4.0"}
    available_fuzzers = ['random', 'shuffle', 'invalid', 'missing', 'insane', 'duplicate', 'lowercase', 'missing_prefix']
    available_categories = ['base', 'temporal', 'environmental', 'supplemental', 'all']
    available_versions = ['2.0', '3.0', '3.1', '4.0']

    parser = argparse.ArgumentParser(description="CVSS Fuzz - for fuzzing CVSS vector strings.")
    parser.add_argument("--count", type=int, required=False, default=default_settings['count'], help="Count of outputs")
    parser.add_argument("--fuzzer", type=str,  choices=available_fuzzers, default=default_settings['fuzzer'], required=False, help="Type of fuzzer")
    parser.add_argument("--category", type=str, choices=available_categories, default=default_settings['category'], required=False, help="Category")
    parser.add_argument("--version", type=str, choices=available_versions, required=False, default=default_settings['version'], help="Version")
    settings = vars(parser.parse_args())

    fuzz = CVSSFuzz(config=settings)
    for fuzzed_value in fuzz.run():
        print(fuzzed_value)  # using print in cli just to get rid of all the logging prefix stuff.

if __name__ == "__main__":
    sys.exit(main())