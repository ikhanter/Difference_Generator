"""Main script and entry point."""
import argparse
from gendiff.modules.gendiff import read_json
from gendiff.modules.gendiff import generate_diff


FORMAT = ('JSON', 'plain')
parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', default=FORMAT, help='set format of output')  # noqa: E501
args = parser.parse_args()


def main():
    """Realize main script of the module."""
    f1, f2 = read_json(args.first_file, args.second_file)
    result = generate_diff(f1, f2)
    return result


if __name__ == '__main__':
    main()
