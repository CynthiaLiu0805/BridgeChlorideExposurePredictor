
import math
import numpy as np
import pandas as pd
from calculation_load import Calculation_load

import calculation_step1
import calculation_step2

import calculation_step3

import calculation_step4
import calculation_step5
import calculation_step6

def savefile(long, lat, results):
    results = np.column_stack((long, lat, results))
    df = pd.DataFrame(results)

    # Generate column headers
    column_headers = ['LON', 'LAT'] + ['{}'.format(i) for i in range(2006, 2101)]

    # Set column headers
    df.columns = column_headers

    # Write to CSV
    df.to_csv('results.csv', index=False)

load = Calculation_load('1.xlsx')
AADT = calculation_step5.updateAADT(load.AADT)
AADTT = calculation_step5.updateAADTT(load.AADTT)
M_app = calculation_step1.calculate(load.h_total, load.t1)
h_app = calculation_step2.calculate(load.h_total, load.t2)
SD_total = calculation_step3.calculate(h_app)
SD_totalCl = calculation_step4.calculate(M_app, h_app, SD_total)

C_s_air = calculation_step5.calculate(SD_totalCl, load.t2, AADT, AADTT)
results = calculation_step6.calculate(C_s_air)
savefile(load.long, load.lat, results)

# print(M_app)