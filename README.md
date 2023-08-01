### Hexlet tests and linter status:
[![Actions Status](https://github.com/ikhanter/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/ikhanter/python-project-50/actions)

### CodeClimate status:
[![Maintainability](https://api.codeclimate.com/v1/badges/13a738a082e82c452efe/maintainability)](https://codeclimate.com/github/ikhanter/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/13a738a082e82c452efe/test_coverage)](https://codeclimate.com/github/ikhanter/python-project-50/test_coverage)

# About

The educational project that generate diff between two JSON-like files and present it in 3 formats:
- Plain style;
- Stylish (nested);
- JSON.

Demos are presented below.

# System requirements

- Python 3.10 or above
- Poetry 1.5.1 or above
- Module argparse 1.4.0 or above
- Module PyYAML 6.0.1 or above

# Installing

All commands should be written without "".
From directory of the repository:
1. "make install"
2. "make build"
3. "make publish"
4. "make package-install"
5. Program works this way: "gendiff *path-to-initial-file* *path-to-new-file*"
6. You can also choose the style of representation: "gendiff *path-to-initial-file* *path-to-new-file* -f stylish(default)/plain/json"
7. You can also try some demos to check outputs more accurately:
  - Plain structures for Stylish output: "make demo_default"
  - Nested structures for Stylish output: "make demo_nested"
  - Nested structures for Plain output: "make demo_plain"
  - Nested structures for JSON output: "make demo_json"


### Stylish Plain demo
[![gendiff demonstration](https://asciinema.org/a/AzJveM1IrhjZrSWMZNQ1O2ZJM.svg)](https://asciinema.org/a/AzJveM1IrhjZrSWMZNQ1O2ZJM)

### Stylish Nested Demo
[![gendiff demonstration](https://asciinema.org/a/VwabiDz7eayEUaMTtzIUFbmBf.svg)](https://asciinema.org/a/VwabiDz7eayEUaMTtzIUFbmBf)

### Plainstyle Nested Demo
[![gendiff demonstration](https://asciinema.org/a/2IuVamvUXahF7X8XEXiuJSacA.svg)](https://asciinema.org/a/2IuVamvUXahF7X8XEXiuJSacA)

### JSON-stile Nested Demo
[![gendiff demonstration](https://asciinema.org/a/9fCbxgZYSxSr7V8MrUoGCHIfb.svg)](https://asciinema.org/a/9fCbxgZYSxSr7V8MrUoGCHIfb)