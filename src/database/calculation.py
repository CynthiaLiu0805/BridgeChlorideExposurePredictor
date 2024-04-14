
import math
import numpy as np
import pandas as pd
from calculation_load import Calculation_load

import deicing_salts_cal
import melted_water_thickness

import single_water_SAS_cal

import single_Cl_SAS_cal
import all_Cl_SAS_cal
import salts_decomposiition_cal

def savefile(long, lat, results):
    results = np.column_stack((long, lat, results))
    df = pd.DataFrame(results)

    # Generate column headers
    column_headers = ['LON', 'LAT'] + ['{}'.format(i) for i in range(2006, 2061)]

    # Set column headers
    df.columns = column_headers

    # Write to CSV
    df.to_csv('results.csv', index=False)

load = Calculation_load('datamodel.xlsx')
AADT = all_Cl_SAS_cal.updateAADT(load.AADT)
AADTT = all_Cl_SAS_cal.updateAADTT(load.AADTT)
M_app = deicing_salts_cal.calculate(load.h_total, load.t1)
h_app = melted_water_thickness.calculate(load.h_total, load.t2)
SD_total = single_water_SAS_cal.calculate(h_app)
SD_totalCl = single_Cl_SAS_cal.calculate(M_app, h_app, SD_total)

C_s_air = all_Cl_SAS_cal.calculate(SD_totalCl, load.t2, AADT, AADTT)
results = salts_decomposiition_cal.calculate(C_s_air)
savefile(load.long, load.lat, results)

# print(M_app)