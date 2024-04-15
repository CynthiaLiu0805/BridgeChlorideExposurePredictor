# Bridge Corrosion Source Code

This folder contains the source code for this project. The structure is as follows:

```
.
├── app
│   ├── exception.py - Store the InputOutofOntario exception
│   ├── input_check.py - Check if the input is valid
│   ├── main.py - The main program to start the app
│   ├── ontario_boundary.geojson - The geojson file used to shape the ontario boundary
│   ├── search.py - Search the input in the database
│   ├── visualization.py - Visual the result to an interactive line graph
│   ├── test_input_check.py
│   ├── test_search.py
│   ├── test_visualization.py
│   └── templates
│       └── index.html - The website template
└── database
    ├── all_Cl_SAS_cal.py -Fifth step of the calculation
    ├── calculation.py - Use the other modules to do the calculation
    ├── calculation_load.py - Load the climate and traffic data for generating the database
    ├── constant.py - Store the constant
    ├── deicing_salts_cal.py - First step of the calculation
    ├── melted_water_thickness.py - Second step of the calculation
    ├── chloride_decomposition_cal.py -Sixth step of the calculation
    ├── single_Cl_SAS_cal.py - Fourth step of the calculation
    ├── single_water_SAS_cal.py - Third step of the calculation
    ├── test_model_input.py 
    └── test_calculation.py 
```