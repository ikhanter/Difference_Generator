import json
import pytest
from gendiff.scripts.gendiff import generate_diff


expected = open('gendiff/tests/fixtures/expected1.txt')
expected_partial, expected_full, expected_null = expected.readlines().split('\n\n\n')
expected.close()


@pytest.fixture
def define_json():
    return (
        json.load(open('gendiff/tests/fixtures/file1.json')),
        json.load(open('gendiff/tests/fixtures/file2.json')),
        json.load(open('gendiff/tests/fixtures/file3.json')),
        json.load(open('gendiff/tests/fixtures/file4.json'))
    )


file1, file2, file3, file4 = define_json()


def test_partial_intersection():
    assert generate_diff(file1, file2) == expected_partial, \
    "Test of partial intersection of JSON files is failed"


def test_full_intersection():
    assert generate_diff(file1, file3) == expected_full, \
    "Test of full intersection of JSON files is failed"


def test_null_intersection():
    assert generate_diff(file1, file4) == expected_null, \
    "Test of null intersection of JSON files is failed"
