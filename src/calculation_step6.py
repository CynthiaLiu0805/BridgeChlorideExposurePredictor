import math
import numpy as np
from constant import Constant
from calculation_load import Calculation_load
from calculation_step1 import Calculation_step1

from calculation_step2 import Calculation_step2
from calculation_step3 import Calculation_step3

from calculation_step4 import Calculation_step4
from calculation_step5 import Calculation_step5


class Calculation_step6:
    def __init__(self, C_s_air):
        self.C_s_air = C_s_air
        self.results = np.zeros((1645, 95))


    def calculate(self):
        # % chloride on bridge surface
        # % d is the distance between road edge and bridge substructure, taken as
        # % 3.5m
        d = Constant.d
        C_spray = self.C_s_air * 0.015
        C_splash = self.C_s_air * 0.985
        self.results = C_spray * math.exp(-0.05*d) + C_splash * math.exp(-0.5*d)


# load = Calculation_load()
# calculation_step1 = Calculation_step1(load.h_total, load.t1)
# calculation_step1.calculate()
# calculation_step2 = Calculation_step2(load.h_total, load.t2)
# calculation_step2.calculate()
# calculation_step3 = Calculation_step3(calculation_step2.h_app)
# calculation_step3.calculate()
# calculation_step4 = Calculation_step4(calculation_step3.h_app, calculation_step1.M_app, calculation_step3.SD_total)
# calculation_step4.calculate()
# calculation_step5 = Calculation_step5(load.AADT, load.AADTT, calculation_step4.SD_totalCl, load.t2)
# # calculation_step5.update_AADT()
# calculation_step5.calculate()
# calculation_step6 = calculation_step6(calculation_step5.C_s_air)
# calculation_step6.calculate()
# print(calculation_step6.results)
# # print(calculation_step5.C_s_air)
