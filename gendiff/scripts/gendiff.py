"""Main script and entry point"""
import argparse
from gendiff.modules.gendiff import generate_diff

FORMAT = ['JSON', 'plain']
parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', default=FORMAT, help='set format of output')
args = parser.parse_args()


def main():
    """Main func"""
    print(args)
    generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
