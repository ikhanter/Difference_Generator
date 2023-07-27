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
	poetry run coverage run -m pytest gendiff/tests/test_gendiff.py

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml