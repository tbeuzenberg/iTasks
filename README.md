# iTasks Desktop Application

[![Build Status](https://travis-ci.org/tbeuzenberg/iTasks.svg?branch=development)](https://travis-ci.org/tbeuzenberg/iTasks)
[![Coverage Status](https://coveralls.io/repos/github/tbeuzenberg/iTasks/badge.svg?branch=development)](https://coveralls.io/github/tbeuzenberg/iTasks?branch=development)

This project is a Desktop Application for the [iTasks framework.](http://www.itasks.org/)

## Requirements

This project uses **Python 3.6**.  
PyQt5 is required and can be installed with Pip (Python package manager):
```commandline
pip install PyQt5
```

## Communication with iTasks

This program supports communication with iTasks over Standard input / Standard output (StdIO).  
Because iTasks does not yet have support for StdIO, a wrapper application is used to test the program.  
The wrapper application is written in C# and can be found at [GitHub](https://github.com/nickhidding/itaskstostdio)

## Installation instructions

1. Download iTasks (Development release) from the [Clean website](http://clean.cs.ru.nl/Download_Clean)
2. Unpack and compile the example iTasks project:
    1. After extracting the .zip, open the map clean-bundle-complete and run CleanIDE.exe
    2. Go to Open > ..\Path\To\clean-bundle-complete\Examples\iTasks\BasicAPIExamples.prj and click 'Open'.
    3. Click on the Update and Run button in the top of the screen.
    4. Close the application.
    5. A BasicAPIExamples.exe.exe is built. Remember the path, since this will be necessary in the next step.

3. [Temporary step] If you don't have an IDE to run C#-applications (Visual Studio/Rider) download the here: [Visual Studio](https://www.visualstudio.com/downloads/)/[Rider](https://www.jetbrains.com/rider/download/#section=windows). If you do, proceed to step 4.

4. [Temporary step] Download the iTasks wrapper project from [GitHub](https://github.com/nickhidding/itaskstostdio) and fill in the correct path to the iTasks executable:
    1. Open iTasksToStdIO.sln and double-click Program.cs
    2. in the code ```p.StartInfo = new ProcessStartInfo("")```, type the path to the BasicAPIExamples.exe.exe from step 2 between the ```""```.
      It look like this: ````p.StartInfo = new ProcessStartInfo("..\Path\To\clean-bundle-complete\Examples\iTasks\BasicAPIExamples.exe.exe")````
    3. Check if the gate for the websocket looks like this for Windows: ``ws://127.0.0.1:80/gui-wsock``  
    and like this for Linux: ``ws://127.0.0.1:8080/gui-wsock``
    4. Run the application.
    5. Close the application and the IDE.
5. [Temporary step] A few files are added to the Debug map of the iTasksToStdIO program. Copy the executable from step 3 to this project in the folder `itasks_server`:
    1. Go to iTasksStdIO > bin > Debug and copy all the files to the map ``itasks_server`` in the Pythonproject.

You can now run the application.
## Usage

The application can be run from the commandline:
```commandline
python main.py
```

It is also possible to run the program from a Python IDE such as Pycharm Community.

## Unit tests

The unit tests are located in the `test` folder.  
The easiest way to run the unit tests is to use Pytest:
```commandline
pytest
```
