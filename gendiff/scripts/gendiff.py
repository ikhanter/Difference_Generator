"""Main script and entry point."""
import argparse

from gendiff.modules.gendiff import generate_diff
from gendiff.modules.loader import read_pair_of_files

FORMAT = ('stylish', 'plain')
parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', default='stylish', choices=FORMAT, help='set format of output')  # noqa: E501
args = parser.parse_args()


def main():
    """
    Realize main script of the module.

    Returns:
        str: String formed as JSON
    """
    f1, f2 = read_pair_of_files(args.first_file, args.second_file)
    if args.format == 'stylish':
        return generate_diff(f1, f2, 'stylish')
    elif args.format == 'plain':
        return generate_diff(f1, f2, 'plain')


if __name__ == '__main__':
    main()
