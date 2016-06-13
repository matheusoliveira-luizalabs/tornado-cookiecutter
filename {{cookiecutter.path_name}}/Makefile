UNAME := $(uname -s)

ifeq ($(UNAME), Linux)
	OPEN_CMD ?= xdg-open
endif
ifeq ($(UNAME), Darwin)
	OPEN_CMD ?= open
endif

APP_NAME={{cookiecutter.path_name}}

TEST_SETTINGS=apps.settings.test
DEV_SETTINGS=apps.settings.development
PROD_SETTINGS=apps.settings.production
SANDBOX_SETTINGS=apps.settings.sandbox

set-pythonpath:
	@PYTHONPATH=$(PYTHONPATH):$(shell pwd)/{{cookicutter.project_slug}}/

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage

install-dev:
	@pip install -r {{cookiecutter.project_slug}}/requirements/development.txt

test: clean set-pythonpath
	@py.test -x -s -v {{cookiecutter.project_slug}}/apps/

test-coverage: clean set-pythonpath
	@py.test -x -s -v --cov={{cookiecutter.project_slug}}/apps/ --cov-config=.coveragerc --cov-report=term --cov-report=html --cov-report=xml

open-coverage: clean set-pythonpath
	$(OPEN_CMD) htmlcov/index.html

provision:
	@ansible

linter: clean
	@flake8 --show-source .

shell:
	@python {{cookiecutter.project_slug}}/shell.py

runserver:
	@python {{cookiecutter.project_slug}}/server.py --settings=$(DEV_SETTINGS)


tsuru-appcreate:
	@tsuru app-create $(APP_NAME) python3

deploy-sandbox: clean set-pythonpath
	@tsuru env-set SIMPLE_SETTINGS=$(SANDBOX_SETTINGS) -a $(APP_NAME)
	@tsuru app-deploy . -a $(APP_NAME)
