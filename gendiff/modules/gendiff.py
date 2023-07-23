"""Module for finding diffs between two json-files."""
import json
import itertools


def stringify(data1, data2, keys):
    replacer = '   '
    prefix = '{'
    suffix = '}'
    lines = []
    lines.append(prefix)
    for key in keys:
        if (key in data1.keys()) and (key in data2.keys()):
            if data1[key] == data2[key]:
                lines.append(f'   {key}: {data1[key]}')
            else:
                lines.append(f' - {key}: {data1[key]}')
                lines.append(f' + {key}: {data2[key]}')
        elif (key in data1.keys()) and not (key in data2.keys()):
            lines.append(f' - {key}: {data1[key]}')
        elif not (key in data1.keys()) and (key in data2.keys()):
            lines.append(f' + {key}: {data2[key]}')
    lines.append(suffix)
    return '\n'.join(lines)


def generate_diff(file1, file2):
    f1 = json.load(open(file1))
    f2 = json.load(open(file2))
    keys_f1 = set(f1.keys())
    keys_f2 = set(f2.keys())
    all_keys = sorted(keys_f1.union(keys_f2))
    result = stringify(f1, f2, all_keys)
    print(result)
