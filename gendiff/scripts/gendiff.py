"""Main script and entry point."""
import argparse

from gendiff.modules.gendiff import generate_diff

FORMAT = ('stylish', 'plain', 'json')
parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', default='stylish', choices=FORMAT, help='set format of output')  # noqa: E501
args = parser.parse_args()


def main():
    """Realize main script of the module."""
    print(generate_diff(args.first_file, args.second_file, args.format))  # noqa: E501, WPS421


if __name__ == '__main__':
    main()
