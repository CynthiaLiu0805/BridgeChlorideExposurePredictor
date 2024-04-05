
import math
import numpy as np
import pandas as pd
from constant import Constant
from calculation_load import Calculation_load
from calculation_step1 import Calculation_step1

from calculation_step2 import Calculation_step2
from calculation_step3 import Calculation_step3

from calculation_step4 import Calculation_step4
from calculation_step5 import Calculation_step5
from calculation_step6 import Calculation_step6


class Calculation:
    def __init__(self, long, lat, results):
        self.long = long
        self.lat = lat
        self.results = results

    def savefile(self):
        self.results = np.column_stack((self.long, self.lat, self.results))
        # Assuming results is a numpy array
        df = pd.DataFrame(self.results)

        # Generate column headers
        column_headers = ['LON', 'LAT'] + ['{}'.format(i) for i in range(2006, 2101)]

        # Set column headers
        df.columns = column_headers

        # Write to CSV
        df.to_csv('results.csv', index=False)
        # np.savetxt('result.csv', self.results, delimiter=',')

load = Calculation_load('1.xlsx')
calculation_step1 = Calculation_step1(load.h_total, load.t1)
calculation_step1.calculate()
calculation_step2 = Calculation_step2(load.h_total, load.t2)
calculation_step2.calculate()
calculation_step3 = Calculation_step3(calculation_step2.h_app)
calculation_step3.calculate()
calculation_step4 = Calculation_step4(calculation_step3.h_app, calculation_step1.M_app, calculation_step3.SD_total)
calculation_step4.calculate()
calculation_step5 = Calculation_step5(load.AADT, load.AADTT, calculation_step4.SD_totalCl, load.t2)
# calculation_step5.update_AADT()
calculation_step5.calculate()
calculation_step6 = Calculation_step6(calculation_step5.C_s_air)
calculation_step6.calculate()
# print(calculation_step6.results)
calculation = Calculation(load.long, load.lat, calculation_step6.results)
# print(calculation.long, calculation.lat)

calculation.savefile()
# print(calculation_step5.C_s_air)