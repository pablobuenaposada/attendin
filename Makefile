venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

format/isort: venv
	venv/bin/isort src

format/black: venv
	venv/bin/black --verbose src

format: venv format/isort format/black

run: venv
	PYTHONPATH=src venv/bin/python src/main.py --username=$(username) --password=$(password) --regexes=$(regexes) --answers=$(answers)

tests: venv
	venv/bin/pip install -r requirements-tests.txt
	PYTHONPATH=src venv/bin/pytest src/tests

docker/build:
	docker build --no-cache	--tag=attendin .

docker/run:
	 docker run -e username=$(username) -e password=$(password) -e regexes=$(regexes) -e answers=$(answers) attendin

docker/tests:
	 docker run attendin /bin/sh -c 'make tests'