# iTasks Desktop Application

[![Build Status](https://travis-ci.org/tbeuzenberg/iTasks.svg?branch=development)](https://travis-ci.org/tbeuzenberg/iTasks)
[![Coverage Status](https://coveralls.io/repos/github/tbeuzenberg/iTasks/badge.svg?branch=development)](https://coveralls.io/github/tbeuzenberg/iTasks?branch=development)

This project is a Desktop Application for the [iTasks framework.](http://www.itasks.org/)

## Requirements

This project uses **Python 3.6**.  
Another requirement is PyQt5 which can be installed with Pip (python package manager):
```commandline
pip install PyQt5
```

## Communication with iTasks

This program supports communication with iTasks over Standard input / Standard output.  
Because iTasks does not yet have support for StdIO, a wrapper application is used to test the program.  
The wrapper application is written in C# and can be found at [GitHub](https://github.com/nickhidding/itaskstostdio)

## Installation instructions

1. Download iTasks (Development release) from the [Clean website](http://clean.cs.ru.nl/Download_Clean)
2. Unpack and compile the example iTasks project
3. [Temporary step] Download the iTasks wrapper project from [GitHub](https://github.com/nickhidding/itaskstostdio) and fill in the correct path to the iTasks executable
4. [Temporary step] Copy the executable from step 3 to this project in the folder `itasks_server`

## Usage

The application can be run from the commandline:
```commandline
python main.py
```

It is also possible to run the program from an python IDE such as Pycharm Community.

## Unit tests

The unit tests are located in the `test` folder.  
The easiest way to run the unit tests is to use Pytest:
```commandline
pytest
```
