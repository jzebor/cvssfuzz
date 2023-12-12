import argparse
import sys
import logging

from cvssfuzz import CVSSFuzz, settings

settings.setup_logging()
LOG = logging.getLogger(__name__)

def main(config):
    fuzz = CVSSFuzz(config=config)
    for fuzzed_value in fuzz():
        print(fuzzed_value)  # using print in cli just to get rid of all the logging prefix stuff.

if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description="Command-line argument parser")
    parser.add_argument("--iterations", type=int, required=False, default=settings.default_settings['iterations'], help="Number of iterations")
    parser.add_argument("--fuzzer", type=str,  default=settings.default_settings['fuzzer'], required=False, help="Type of fuzzer")
    parser.add_argument("--category", type=str, default=settings.default_settings['category'], required=False, help="Category")
    parser.add_argument("--version", type=str, required=False, default=settings.default_settings['version'], help="Version")
    settings = vars(parser.parse_args())
    sys.exit(main(config=settings))