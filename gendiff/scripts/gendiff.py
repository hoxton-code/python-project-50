#!/usr/bin/env python3
from gendiff.diff import generate_diff
from gendiff.arg_parser import create_parser


def main():
    """
    Run the file comparison tool's main logic.

    Parses command-line arguments, generates a diff, and prints it.

    Command-line arguments should include two file paths and can
    optionally include a formatter name.
    """

    parser = create_parser()
    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    formatter = args.format
    diff = generate_diff(first_file, second_file, formatter)
    print(diff)


if __name__ == '__main__':
    main()
