import numpy as np
from constant import Constant




def calculate(M_app, h_app, SD_total):
        salt_to_water_ratio = M_app / (h_app * Constant.water_density)
        # print(salt_to_water_ratio)
        SD_totalCl = SD_total * salt_to_water_ratio * Constant.chloride_ratio
        return SD_totalCl
