import argparse


def create_parser():
    """
    Create an ArgumentParser for the file comparison tool.

    Requires two file paths and an optional output format argument.

    Returns:
    Configured ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f', '--format', help="set format of output")
    return parser
