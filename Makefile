init:
	python3 -m venv .venv
	. .venv/bin/activate

install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	#python -m pytest -vv --cov=myrepolib tests/*.py
	#python -m pytest --nbval notebook.ipynb


lint:
	pylint --disable=R,C main.py

all: install lint test