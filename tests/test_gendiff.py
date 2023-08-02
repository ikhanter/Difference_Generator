"""Test module for gendiff."""
import json

from gendiff.modules.gendiff import generate_diff

with open('tests/fixtures/expected/expected_plain.txt') as expected:
    expected_partial, expected_full, expected_null = (''.join(expected.readlines()).split('\n\n\n'))  # noqa: E501

with open('tests/fixtures/expected/expected_nested.txt') as expected:
    expected_nested_json, expected_nested_both, expected_nested_yaml = (''.join(expected.readlines()).split('\n\n\n'))  # noqa: E501

with open('tests/fixtures/expected/expected_nested_plainstyle.txt') as expected:
    expected_plainstyle_json, expected_plainstyle_both, expected_plainstyle_yaml = (''.join(expected.readlines()).split('\n\n\n'))  # noqa: E501

with open('tests/fixtures/expected/expected_nested_jsonstyle1.json') as expected:
    expected_jsonstyle_json = json.load(expected)

with open('tests/fixtures/expected/expected_nested_jsonstyle2.json') as expected:
    expected_jsonstyle_both = json.load(expected)

with open('tests/fixtures/expected/expected_nested_jsonstyle3.json') as expected:
    expected_jsonstyle_yaml = json.load(expected)  # noqa: E501

# JSON plain
f1_json, f2_json, f3_json, f4_json = (
    'tests/fixtures/files/file1.json',
    'tests/fixtures/files/file2.json',
    'tests/fixtures/files/file3.json',
    'tests/fixtures/files/file4.json',
)

# YAML plain
f1_yaml, f2_yaml, f3_yaml, f4_yaml = (
    'tests/fixtures/files/file1.yml',
    'tests/fixtures/files/file2.yaml',
    'tests/fixtures/files/file3.yml',
    'tests/fixtures/files/file4.yaml',
)

# JSON/YAML nested
f1_json_nested, f2_json_nested, f3_yaml_nested, f4_yaml_nested = (
    'tests/fixtures/files/file1_nested.json',
    'tests/fixtures/files/file2_nested.json',
    'tests/fixtures/files/file3_nested.yaml',
    'tests/fixtures/files/file4_nested.yml',
)


def test_flat_intersection():
    """Test function with flat JSON and YAML files."""
    assert generate_diff(f1_json, f2_json, 'stylish') == expected_partial, \
        'Test of partial intersection of JSON files is failed'  # noqa: S101, N400, E501
    assert generate_diff(f1_json, f3_json, 'stylish') == expected_full, \
        'Test of full intersection of JSON files is failed'  # noqa: S101, N400
    assert generate_diff(f1_json, f4_json, 'stylish') == expected_null, \
        'Test of null intersection of JSON files is failed'  # noqa: S101, N400
    assert generate_diff(f1_yaml, f2_yaml, 'stylish') == expected_partial, \
        'Test of partial intersection of YAML files is failed'  # noqa: S101, N400, E501
    assert generate_diff(f1_yaml, f3_yaml, 'stylish') == expected_full, \
        'Test of full intersection of YAML files is failed'  # noqa: S101, N400
    assert generate_diff(f1_yaml, f4_yaml, 'stylish') == expected_null, \
        'Test of null intersection of YAML files is failed'  # noqa: S101, N400


def test_nested_intersection():
    """Test function with nested JSON and YAML files."""
    assert generate_diff(f1_json_nested, f2_json_nested, 'stylish') == expected_nested_json, \
    'Test of nested intersection of JSON files is failed'  # noqa: S101, N400
    assert generate_diff(f1_json_nested, f3_yaml_nested, 'stylish') == expected_nested_both, \
    'Test of nested intersection of JSON/YAML files is failed'  # noqa: S101, N400
    assert generate_diff(f3_yaml_nested, f4_yaml_nested, 'stylish') == expected_nested_yaml, \
    'Test of nested intersection of YAML files is failed'  # noqa: S101, N400


def test_plainstyle_intersection():
    """Test function with nested JSON and YAML files for plain style."""
    assert generate_diff(f1_json_nested, f2_json_nested, 'plain') == expected_plainstyle_json, \
    'Test of plainstyle intersection of JSON files is failed'  # noqa: S101, N400
    assert generate_diff(f1_json_nested, f3_yaml_nested, 'plain') == expected_plainstyle_both, \
    'Test of plainstyle intersection of JSON/YAML files is failed'  # noqa: S101, N400
    assert generate_diff(f3_yaml_nested, f4_yaml_nested, 'plain') == expected_plainstyle_yaml, \
    'Test of plainstyle intersection of YAML files is failed'  # noqa: S101, N400


def test_jsonstyle_intersection():
    """Test function with nested JSON and YAML files for JSON style."""
    assert generate_diff(f1_json_nested, f2_json_nested, 'json') == json.dumps(expected_jsonstyle_json, indent=2), \
    'Test of JSON-style intersection of JSON files is failed'  # noqa: S101, N400
    assert generate_diff(f1_json_nested, f3_yaml_nested, 'json') == json.dumps(expected_jsonstyle_both, indent=2), \
    'Test of JSON-style intersection of JSON/YAML files is failed'  # noqa: S101, N400
    assert generate_diff(f3_yaml_nested, f4_yaml_nested, 'json') == json.dumps(expected_jsonstyle_yaml, indent=2), \
    'Test of JSON-style intersection of YAML files is failed'  # noqa: S101, N400