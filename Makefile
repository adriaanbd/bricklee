install:
	pip install --upgrade pip
	pip install poetry
	poetry install -vvv

test:
	python -m unittest
	python -m behave

build:
	poetry build -vvv

patch:
	poetry version patch

testpypi_config:
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry config http-basic.testpypi $TEST_PYPI_USERNAME $TEST_PYPI_PASSWORD

publish_test:
	poetry publish -r testpypi

publish:
	poetry publish
