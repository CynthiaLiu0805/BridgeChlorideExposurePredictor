# Bridge Corrosion

Developer Names: Cynthia Liu
Theory support: Mingsai Xu

Date of project start: January 19, 2024

This project is intended to investigate how climate, traffic might impact corrosion-induced damage for reinforced concrete bridges by influencing the chloride exposure.

The folders and files for this project are as follows:

docs - Documentation for the project
refs - Reference material used for the project
src - Source code
test - Test cases

## Set Up

### Python
This project is based on Python. To install Python in windows, simply download the release from [here](https://www.python.org/downloads/windows/) and follow the install instructions.\
To install Python on mac, you can download the release from [here](https://www.python.org/downloads/macos/).



### Make
This project use [make](https://www.gnu.org/software/make/manual/make.html#Overview) as an access for running the software. 

To install make in windows, you can do 
`winget install ezwinports.make` in PowerShell. \
To install make in mac, do `brew install make` if you have [Homebrew](https://brew.sh/) installed. It is also available in other package managers.

## How to Start

1. Download the zip file of this repo.
2. Open the command line terminal (for mac) or PowerShell (for windows).
3. Do `make requirements` in the root folder to install the libraries and dependencies.
4. Do  `make database` to generate the chloride exposure database.
5. Do  `make app` to run the software. 
6. You should see the message from terminal saying that the software is running successfully in localhost. Usually it is http://127.0.0.1:5000 but it might differ from machines.

### Alternative ways to run
If the above method does not work, you can try the following:
```
cd src
python calculation.py
python main.py
```
Then the software should be running in localhost.


Notes: In some Python versions, you might need to do python3 instead of python to run the app. That is:
```
cd src
python3 calculation.py
python3 main.py
```
