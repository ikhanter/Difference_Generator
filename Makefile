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

demo:
	gendiff tests/fixtures/file1_nested.json tests/fixtures/file3_nested.yaml