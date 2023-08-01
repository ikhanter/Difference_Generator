lint:
	poetry run flake8 gendiff

install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

demo_default:
	gendiff tests/fixtures/files/file1.json tests/fixtures/files/file2.json

demo_nested:
	gendiff tests/fixtures/files/file1_nested.json tests/fixtures/files/file3_nested.yaml

demo_plain:
	gendiff tests/fixtures/files/file1_nested.json tests/fixtures/files/file3_nested.yaml -f plain

demo_json:
	gendiff tests/fixtures/files/file1_nested.json tests/fixtures/files/file3_nested.yaml -f json