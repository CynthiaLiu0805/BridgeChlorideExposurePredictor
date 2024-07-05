'''
This module does the calculation for chloride exposure rate and generate the database
'''
import numpy as np
import pandas as pd
from calculation_load import Calculation_load
import deicing_salts_cal
import melted_water_thickness
import single_water_SAS_cal
import single_Cl_SAS_cal
import all_Cl_SAS_cal
import chloride_on_pier
from constant import Constant
import chloride_on_deck

def savefile(long, lat, results, filename):
    # Put longitude and latitude together
    results = np.column_stack((long, lat, results))
    df = pd.DataFrame(results)

    # Generate column headers
    column_headers = ['LON', 'LAT'] + ['{}'.format(i) for i in range(2006, 2061)]

    # Set column headers
    df.columns = column_headers

    # Write to CSV
    df.to_csv(filename, index=False)

# Use all the other modules to generate the database
load = Calculation_load('datamodel.xlsx')
AADT = all_Cl_SAS_cal.updateAADT(load.AADT)
AADTT = all_Cl_SAS_cal.updateAADTT(load.AADTT)
# For high salt application rate
M_app_high = deicing_salts_cal.calculate(load.h_total, load.t1, Constant.salt_application_rate_high)
h_app = melted_water_thickness.calculate(load.h_total, load.t2)
SD_total = single_water_SAS_cal.calculate(h_app)
SD_totalCl_high = single_Cl_SAS_cal.calculate(M_app_high, h_app, SD_total)
C_s_air_high = all_Cl_SAS_cal.calculate(SD_totalCl_high, load.t2, AADT, AADTT)
pier_high = chloride_on_pier.calculate(C_s_air_high)
savefile(load.long, load.lat, pier_high, "pier_high.csv")
# For low salt application rate
M_app_low = deicing_salts_cal.calculate(load.h_total, load.t1, Constant.salt_application_rate_low)
h_app = melted_water_thickness.calculate(load.h_total, load.t2)
SD_total = single_water_SAS_cal.calculate(h_app)
SD_totalCl_low = single_Cl_SAS_cal.calculate(M_app_low, h_app, SD_total)
C_s_air_low = all_Cl_SAS_cal.calculate(SD_totalCl_low, load.t2, AADT, AADTT)
pier_low = chloride_on_pier.calculate(C_s_air_low)
savefile(load.long, load.lat, pier_low, "pier_low.csv")

deck = chloride_on_deck.deck_calculation(load.h_total, AADT)
savefile(load.long, load.lat, deck, "deck.csv")
