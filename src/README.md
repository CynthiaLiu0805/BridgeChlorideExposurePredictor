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
│   ├── test_input_check.py - Test
│   ├── test_search.py
│   ├── test_visualization.py
│   └── templates
│       └── index.html
└── database
    ├── all_Cl_SAS_cal.py
    ├── calculation.py
    ├── calculation_load.py
    ├── constant.py
    ├── deicing_salts_cal.py
    ├── melted_water_thickness.py
    ├── salts_decomposiition_cal.py
    ├── single_Cl_SAS_cal.py
    ├── single_water_SAS_cal.py
    └── test_calculation.py
```