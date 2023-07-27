"""Test module for gendiff."""
import json, yaml
from gendiff.modules.gendiff import generate_diff, read_pair_of_files

with open('tests/fixtures/expected1.txt') as expected:
    expected_partial, expected_full, expected_null = (''.join(expected.readlines()).split('\n\n\n'))  # noqa: E501

# JSON plain
file1, file2, file3, file4 = (
    'tests/fixtures/file1.json',
    'tests/fixtures/file2.json',
    'tests/fixtures/file3.json',
    'tests/fixtures/file4.json',
)

# YAML plain
file5, file6, file7, file8 = (
    'tests/fixtures/file1.yml',
    'tests/fixtures/file2.yaml',
    'tests/fixtures/file3.yml',
    'tests/fixtures/file4.yaml',
)


f1_json, f2_json = read_pair_of_files(file1, file2)
f3_json, f4_json = read_pair_of_files(file3, file4)
f1_yaml, f2_yaml = read_pair_of_files(file5, file6)
f3_yaml, f4_yaml = read_pair_of_files(file7, file8)


def test_read_pair_of_files():
    """Test for read_pair_of_files."""
    assert read_pair_of_files('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == \
    (json.load(open('tests/fixtures/file1.json')), json.load(open('tests/fixtures/file2.json'))), \
    'Test of read_pair_of_files for JSON is failed'
    assert read_pair_of_files('tests/fixtures/file1.yml', 'tests/fixtures/file2.yaml') == \
    (yaml.safe_load(open('tests/fixtures/file1.json')), yaml.safe_load(open('tests/fixtures/file2.json'))), \
    'Test of read_pair_of_files for YAML is failed'


def test_flat_intersection():
    """Test function with flat JSON and YAML files."""
    assert generate_diff(f1_json, f2_json) == expected_partial, \
        'Test of partial intersection of JSON files is failed'  # noqa: S101, N400, E501
    assert generate_diff(f1_json, f3_json) == expected_full, \
        'Test of full intersection of JSON files is failed'  # noqa: S101, N400
    assert generate_diff(f1_json, f4_json) == expected_null, \
        'Test of null intersection of JSON files is failed'  # noqa: S101, N400
    assert generate_diff(f1_yaml, f2_yaml) == expected_partial, \
        'Test of partial intersection of YAML files is failed'  # noqa: S101, N400, E501
    assert generate_diff(f1_yaml, f3_yaml) == expected_full, \
        'Test of full intersection of YAML files is failed'  # noqa: S101, N400
    assert generate_diff(f1_yaml, f4_yaml) == expected_null, \
        'Test of null intersection of YAML files is failed'  # noqa: S101, N400

