"""Main script and entry point"""
import argparse

parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')  # noqa: E501
parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
args = parser.parse_args()


def main():
    """Main func"""
    pass


if __name__ == '__main__':
    main
