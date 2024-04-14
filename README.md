# Bridge Corrosion

Developer Names: Cynthia Liu

Theory support: Mingsai Xu

Date of project start: January 19, 2024

This project is intended to investigate how climate, traffic might impact corrosion-induced damage for reinforced concrete bridges by influencing the chloride exposure.


The folders and files for this project are as follows:\
    .\
    ├── doc\                    
    │   ├── SRS\                
    │   ├── VnVPlan\         
    |   ├── Design\
    │   |   ├── SoftArchitecture\
    │   │   └── SoftDetailedDes\ 
    │   └── VnVReport\                
    │── src\          
    |   ├── app         # code for user side of the software\
    │   │   └── test\ 
    │   └── database    # code for generating the database\
    │        └── test\
    │── Makefile\            
    │── requirements.txt    # dependencies\
    └── datamodel.xlsx      # traffic model and climate model\

## Set Up

### Python
This project is based on Python. To install Python in windows, simply download the release from [here](https://www.python.org/downloads/windows/) and follow the install instructions.\
To install Python on mac, you can download the release from [here](https://www.python.org/downloads/macos/).



### Make
This project use [make](https://www.gnu.org/software/make/manual/make.html#Overview) as an access for running the software. 

To install make in windows, you can do 
`winget install ezwinports.make` in PowerShell. \
To install make in mac, do `brew install make` if you have [Homebrew](https://brew.sh/) installed. It is also available in other package managers.\ 
After installation, restart PowerShell or Terminal to make it work.

## How to Start

1. Download and unzip the zip file of this repo.
2. Open the command line terminal (for mac) or PowerShell (for windows).
3. Do `make requirements` in the root folder of this repo to install the libraries and dependencies.
4. Do  `make database` to generate the chloride exposure database.
5. Do  `make app` to run the software. 
6. You should see the message from terminal saying that the software is running successfully in localhost. Usually it is http://127.0.0.1:5000 but it might differ from machines.

### Alternative ways to run
If the above method does not work, you can try the following in the root folder of this repo:
```
python src/database/calculation.py
python src/user/main.py
```
Then the software should be running in localhost.


Notes: In some Python versions, you might need to do python3 instead of python to run the app. That is:
```
python3 src/database/calculation.py
python3 src/user/main.py
```

## Quit
Press `Command+ C` in terminal and `Ctrl + C` in PowerShell to quit the software.



The folders and files for this project are as follows:
# src

* [app/](.\src\app)
  * [templates/](.\src\app\templates)
    * [index.html](.\src\app\templates\index.html)
  
  * [exception.py](.\src\app\exception.py)
  * [input_check.py](.\src\app\input_check.py)
  * [main.py](.\src\app\main.py)
  * [ontario_boundary.geojson](.\src\app\ontario_boundary.geojson)
  * [search.py](.\src\app\search.py)
  * [test_input_check.py](.\src\app\test_input_check.py)
  * [test_search.py](.\src\app\test_search.py)
  * [test_visualization.py](.\src\app\test_visualization.py)
  * [visualization.py](.\src\app\visualization.py)
* [database/](.\src\database)
  * [all_Cl_SAS_cal.py](.\src\database\all_Cl_SAS_cal.py)
  * [calculation.py](.\src\database\calculation.py)
  * [calculation_load.py](.\src\database\calculation_load.py)
  * [constant.py](.\src\database\constant.py)
  * [deicing_salts_cal.py](.\src\database\deicing_salts_cal.py)
  * [melted_water_thickness.py](.\src\database\melted_water_thickness.py)
  * [salts_decomposiition_cal.py](.\src\database\salts_decomposiition_cal.py)
  * [single_Cl_SAS_cal.py](.\src\database\single_Cl_SAS_cal.py)
  * [single_water_SAS_cal.py](.\src\database\single_water_SAS_cal.py)
  * [test_calculation.py](.\src\database\test_calculation.py)
