lint:
	poetry run flake8 gendiff

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

test:
	poetry run gendiff ./gendiff/tests/json/file1.json ./gendiff/tests/json/file2.json