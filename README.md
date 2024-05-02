### Hexlet tests and linter status:
[![Actions Status](https://github.com/hoxton-code/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/hoxton-code/python-project-50/actions)
[![Actions Status](https://github.com/hoxton-code/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/hoxton-code/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/9f097a8350debc570b49/maintainability)](https://codeclimate.com/github/hoxton-code/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/9f097a8350debc570b49/test_coverage)](https://codeclimate.com/github/hoxton-code/python-project-50/test_coverage)

This is the second tutorial project for Python developers as part of a course on [hexlet.io](https://ru.hexlet.io/programs/python/projects/50)
# Difference Calculator
Difference Calculator is a program that determines differences between two data structures based on JSON and YAML files.
Three views are available for output for easy analysis.

## Features
- Support for Multiple Input Formats: The utility can handle both YAML and JSON formats, accommodating a wide range of use cases.
- Versatile Report Generation: Users can generate reports in three different formats for convenience and clarity:
  - Plain Text: A straightforward text summary of the differences.
  - Stylish: A more structured and visually appealing representation of the changes.
  - JSON: A JSON-formatted report


## Requirements
- Python ^3.11
- Poetry
- Make
## Installation
```
git clone https://github.com/hoxton-code/python-project-50.git
make install
make build
make package-install
```
## Usage
### Plain files differences: (Stylish formatter)
[![asciicast](https://asciinema.org/a/M9OuvEjA5ZwuxqwB8DRUWOizD.svg)](https://asciinema.org/a/M9OuvEjA5ZwuxqwB8DRUWOizD)
### Differences of files with nested structure (Stylish formatter):
[![asciicast](https://asciinema.org/a/uoq0WmsgdcpG3jsTGHOULc5Gk.svg)](https://asciinema.org/a/uoq0WmsgdcpG3jsTGHOULc5Gk)
### Plain formatter:
[![asciicast](https://asciinema.org/a/h59Fq6CopKYIT2Vcw6pTHooIK.svg)](https://asciinema.org/a/h59Fq6CopKYIT2Vcw6pTHooIK)
### Json formatter:
[![asciicast](https://asciinema.org/a/TxLQV7bl4LhIPptIkfqQk2LeU.svg)](https://asciinema.org/a/TxLQV7bl4LhIPptIkfqQk2LeU)
