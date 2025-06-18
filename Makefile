#!/bin/bash

.PHONY: build test clean docs venv script env

# Settings
SHELL := /bin/bash
.DEFAULT_GOAL := info
PACKAGE_FOLDER := mof_circular_105_2020

env:
	hatch env create

deps:
	@hatch dep show requirements;

install-dep:
	@python -m pip install -e .;

install:
	@python -m pip install $$(hatch dep show requirements);

install-dev: install
	@python -m pip install -r requirements-dev.txt;

pre-commit-activate:
	@pre-commit install;

ruff:
	@hatch run ruff check ${PACKAGE_FOLDER};

build:
	@hatch build;

test:
	@hatch run test;

docs:
	@hatch run docs;

docs-serve:
	@hatch run docs-serve;

info:
	@echo -e "==============================================================================="
	@echo -e "Package:\t\t\e[34m[MOF] Implement Circular 105/2020\e[0m"
	@echo -e "On version:\t\t\e[34m$$(hatch version)\e[0m"
	@echo -e "==============================================================================="
	@echo -e ""
	@echo -e "> Supported target ============================================================"
	@echo -e "make info: \t\tGet info of the package"
	@echo -e "make install-dev: \tInstall development dependencies"
	@echo -e "make ruff: \t\tLinter and code formatter, written in Rust"
	@echo -e "make docs: \t\tServing local development documentation"
	@echo -e "make test: \t\tTest services"
	@echo -e "make clean: \t\tCleaning bytes codes, cached folder and self generated output"
	@echo -e ""

# Ref: https://cli.github.com/manual/gh_release_list
info-release:
	@gh release list --exclude-drafts --exclude-pre-releases --repo "thuyetbao/mof-circular-105-2020"

# Current: not supported "--json"
info-release-latest:
	@gh release list --exclude-drafts --exclude-pre-releases --repo "thuyetbao/mof-circular-105-2020" --limit 1

release:
	gh release create "v$$(hatch version)";

clean:
	@echo "";
	@echo -e "\e[34m[A] Removed self-generated folder by dependencies or package itself\e[0m";
	@echo -e "\t[+] Remove folders: \`dist\`, \`build\`, \`logs\`";
	@if [ -d dist ] ; then rm -r dist; fi;
	@if [ -d build ] ; then rm -r build; fi;
	@if [ -d logs ] ; then rm -r logs; fi;
	@echo -e "\t[+] Remove egg-info";
	@find ./ -type f -name '*.egg-info' -delete;
	@echo "";
	@echo -e "\e[34m[B] Removing packages folders\e[0m";
	@echo -e "\e[34m[1] Cleaning bytecode in current directory tree...\e[0m";
	@pyclean -v .;
	@echo -e "\t[+] Remove cache from \`pytest\` module";
	@find ./ -maxdepth 1 -type d -name '.pytest_cache' | xargs --no-run-if-empty rm -rf;
	@echo -e "\t[+] Remove cache from \`ruff\` module";
	@find ./ -maxdepth 1 -type d -name '.ruff_cache' | xargs --no-run-if-empty rm -rf;
	@echo -e "\t[+] Remove coverage test";
	@find ./ -type f -name '*.coverage' -delete;
	@echo "";
	@echo -e "\e[32m[Status] Cleared successfully\e[0m";
