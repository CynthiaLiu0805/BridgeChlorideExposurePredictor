import numpy as np
from constant import Constant
from calculation_load import Calculation_load
from calculation_step1 import Calculation_step1

from calculation_step2 import Calculation_step2
from calculation_step3 import Calculation_step3



class Calculation_step4:
    def __init__(self, h_app, M_app, SD_total):
        self.h_app = h_app
        self.M_app = M_app
        self.SD_total = SD_total
        self.SD_totalCl = np.zeros((1645, 95))


    # % mass of chloride ions by one truck
    # % ratio of the mass of salt applied per unit area of road to the mass 
    # % of water per unit area of road
    # % chloride ratio = 0.61
    def calculate(self):
        salt_to_water_ratio = self.M_app / (self.h_app * Constant.water_density)
        # print(salt_to_water_ratio)
        self.SD_totalCl = self.SD_total * salt_to_water_ratio * Constant.chloride_ratio


# load = Calculation_load()
# calculation_step1 = Calculation_step1(load.h_total, load.t1)
# calculation_step1.calculate()
# calculation_step2 = Calculation_step2(load.h_total, load.t2)
# calculation_step2.calculate()
# calculation_step3 = Calculation_step3(calculation_step2.h_app)
# calculation_step3.calculate()
# calculation_step4 = Calculation_step4(calculation_step3.h_app, calculation_step1.M_app, calculation_step3.SD_total)
# calculation_step4.calculate()
# print(calculation_step4.SD_totalCl)