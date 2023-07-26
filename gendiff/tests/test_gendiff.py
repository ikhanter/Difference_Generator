"""Test module for gendiff."""
import json
from gendiff.modules.gendiff import generate_diff
from gendiff.modules.gendiff import read_json


with open('gendiff/tests/fixtures/expected1.txt') as expected:
    expected_partial, expected_full, expected_null = (''.join(expected.readlines()).split('\n\n\n'))  # noqa: E501

file1, file2, file3, file4 = (
    'gendiff/tests/fixtures/file1.json',
    'gendiff/tests/fixtures/file2.json',
    'gendiff/tests/fixtures/file3.json',
    'gendiff/tests/fixtures/file4.json',
    )


f1, f2 = read_json(file1, file2)
f3, f4 = read_json(file3, file4)

def test_partial_intersection():
    """Test function with partial intersection of JSON files."""
    assert generate_diff(f1, f2) == expected_partial, \
        'Test of partial intersection of JSON files is failed'  # noqa: S101, N400, E501


def test_full_intersection():
    """Test function with full intersection of JSON files."""
    assert generate_diff(f1, f3) == expected_full, \
        'Test of full intersection of JSON files is failed'  # noqa: S101, N400


def test_null_intersection():
    """Test function with no intersection of JSON files."""
    assert generate_diff(f1, f4) == expected_null, \
        'Test of null intersection of JSON files is failed'  # noqa: S101, N400
