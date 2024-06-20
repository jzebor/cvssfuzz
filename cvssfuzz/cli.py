import argparse
import sys
import logging

from cvssfuzz import CVSSFuzz, CVSSGenerate

def main1():
    default_settings = {"fuzz": {"count": 5, "fuzzer": "random", "category": "base", "version": "4.0"},
                        "generate": {"category": "base", "version": "4.0"}} # default settings for fuzz and generate commands
    available_fuzzers = ['random', 'shuffle', 'invalid', 'missing', 'insane', 'duplicate', 'lowercase', 'missing_prefix']
    available_categories = ['base', 'temporal', 'environmental', 'supplemental', 'all']
    available_versions = ['2.0', '3.0', '3.1', '4.0']

    parser = argparse.ArgumentParser(description="CVSS Fuzz - for fuzzing CVSS vector strings.")
    parser.add_argument("--count", type=int, required=False, default=default_settings['fuzz']['count'], help="Count of outputs")
    parser.add_argument("--fuzzer", type=str,  choices=available_fuzzers, default=default_settings['fuzz']['fuzzer'], required=False, help="Type of fuzzer")
    parser.add_argument("--category", type=str, choices=available_categories, default=default_settings['fuzz']['category'], required=False, help="Category")
    parser.add_argument("--version", type=str, choices=available_versions, required=False, default=default_settings['fuzz']['version'], help="Version")
    settings = vars(parser.parse_args())

    fuzz = CVSSFuzz(config=settings)
    for fuzzed_value in fuzz.run():
        print(fuzzed_value)  # using print in cli just to get rid of all the logging prefix stuff.


def main():
    default_settings = {"count": 5, "fuzzer": "random", "category": "base", "version": "4.0"}
    available_fuzzers = ['random', 'shuffle', 'invalid', 'missing', 'insane', 'duplicate', 'lowercase', 'missing_prefix', "missing_metric_key", "missing_metric_value"]
    available_categories = ['base', 'threat', 'temporal', 'environmental', 'supplemental', 'all']
    available_versions = ['2.0', '3.0', '3.1', '4.0']
    parser = argparse.ArgumentParser(description="CVSS Fuzz - for fuzzing CVSS vector strings.")

    subparsers = parser.add_subparsers(dest='command', required=True, help='Command to execute')
    # Sub-parser for 'fuzz' command
    fuzz_parser = subparsers.add_parser('fuzz', help='Fuzz CVSS vectors')
    fuzz_parser.add_argument("--count", type=int, required=False, default=default_settings['count'], help="Count of outputs")
    fuzz_parser.add_argument("--fuzzer", type=str, choices=available_fuzzers, default=default_settings['fuzzer'], required=False, help="Type of fuzzer")
    fuzz_parser.add_argument("--category", type=str, choices=available_categories, default=default_settings['category'], required=False, help="Category")
    fuzz_parser.add_argument("--version", type=str, choices=available_versions, required=False, default=default_settings['version'], help="Version")

    # Sub-parser for 'generate' command
    generate_parser = subparsers.add_parser('generate', help='Generate all CVSS vectors')
    generate_parser.add_argument("--category", type=str, choices=available_categories, default=default_settings['category'], required=True, help="Category")
    generate_parser.add_argument("--version", type=str, choices=available_versions, required=True, default=default_settings['version'], help="Version")

    args = parser.parse_args()

    if args.command == 'fuzz':
        # Handle fuzz mode
        fuzz = CVSSFuzz(config={
            'count': args.count,
            'fuzzer': args.fuzzer,
            'category': args.category,
            'version': args.version
        })
        for fuzzed_value in fuzz.run():
            print(fuzzed_value)  # using print in CLI just to get rid of all the logging prefix stuff.

    elif args.command == 'generate':
        raise NotImplementedError("Generate command is not implemented yet.")
        generator = CVSSGenerate(category=args.category, version=args.version)
        for generated_vector in generator.run():
            print(generated_vector)
        # Handle generate mode
        # generate_category = args.category
        # generate_version = args.version
        # # Perform generation logic here
        # print(f"Generating all CVSS vectors for category '{generate_category}' and version '{generate_version}'")

if __name__ == "__main__":
    sys.exit(main())