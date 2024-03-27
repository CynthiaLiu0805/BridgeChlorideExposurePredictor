

import numpy as np
from calculation_load import Calculation_load
from calculation_step2 import Calculation_step2
from constant import Constant


class Calculation_step3:
    def __init__(self, h_app):
        self.h_app = np.array(h_app)
        # self.MR_CA = 0
        # self.MR_TP = np.zeros((1645, 95))
        # self.MR_BW = np.zeros((1645, 95))
        self.SD_total = np.zeros((1645, 95))

    def calculate(self):
        # print(self.h_app)
        # % V_speed is taken as 100km/h
        # % b is the tire width, taken as 0.56 m
        # % K is the ratio of the tire width that is not a groove to the tire
        # % width, taken as 0.75
        # % h_film is the depth of the water film picked up in each rotation, 0.0001 m
        # % water_density is 997 kg/M^3
        # % MR stands for mass flow rate
        V_speed = Constant.V_speed/3.6

        MR_CA = V_speed * Constant.b * Constant.K * Constant.h_film * Constant.water_density
        MR_TP = V_speed * Constant.b * (1-Constant.K) * self.h_app * Constant.water_density
        MR_BW = 0.5 * V_speed * Constant.b *(self.h_app-(Constant.K*Constant.h_film)-((1-Constant.K) * self.h_app)) * Constant.water_density
        MR_SW = 0.5 * V_speed * Constant.b *(self.h_app-(Constant.K*Constant.h_film)-((1-Constant.K) * self.h_app)) * Constant.water_density
        # print(self.M_total)


        # % SD stands for spray density
        # % V is the speed limit in miles/hour, taken as 62?
        V = Constant.V
        SD_CA = (-2.69 * 10**(-5) * V + 2.43 * 10**(-3)) * MR_CA
        SD_TP = (1.16 * 10**(-5) * V - 5.25 * 10**(-5)) * MR_TP
        SD_BW = (2.67 * 10**(-5) * V - 4.71 * 10**(-4)) * MR_BW
        SD_SW = (1.65 * 10**(-5) * V - 3.99 * 10**(-4)) * MR_SW

        self.SD_total = SD_CA + SD_TP + SD_BW + SD_SW



# load = Calculation_load()
# last = Calculation_step2(load.h_total, load.t2)
# last.calculate()
# calculation_step3 = Calculation_step3(last.h_app)
# calculation_step3.calculate()
# print(calculation_step3.SD_total)
# print(calculation_step3.MR_CA, "tp", calculation_step3.MR_TP, "bw", calculation_step3.MR_BW, "sw",calculation_step3.MR_SW)