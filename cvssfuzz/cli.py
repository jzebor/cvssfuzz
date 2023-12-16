import argparse
import sys
import logging

from cvssfuzz import CVSSFuzz, settings

def main():
    default_settings = {"iterations": 5, "fuzzer": "random", "category": "base", "version": "4.0"}
    parser = argparse.ArgumentParser(description="CVSS Fuzz - for fuzzing CVSS vector strings.")
    parser.add_argument("--iterations", type=int, required=False, default=default_settings['iterations'], help="Number of iterations")
    parser.add_argument("--fuzzer", type=str,  default=default_settings['fuzzer'], required=False, help="Type of fuzzer")
    parser.add_argument("--category", type=str, default=default_settings['category'], required=False, help="Category")
    parser.add_argument("--version", type=str, required=False, default=default_settings['version'], help="Version")
    settings = vars(parser.parse_args())

    fuzz = CVSSFuzz(config=settings)
    for fuzzed_value in fuzz.run():
        print(fuzzed_value)  # using print in cli just to get rid of all the logging prefix stuff.

if __name__ == "__main__":
    sys.exit(main())