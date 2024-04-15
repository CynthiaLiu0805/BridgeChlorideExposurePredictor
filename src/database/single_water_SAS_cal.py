'''
This module provides third step of the database generation. It is related to GD1, GD2, DD4 in SRS.
Output: SD_total: the water sprayed and splashed by one truck
Input:  h_app: the thickness of melted water per day with snow melting
Constant: 
        V_speed: speed limit in km/h
        b: the tire width
        K: the ratio of the tire width that is not a groove to the tire width
        h_film: the depth of the water film picked up in each rotation
        water_density: water density
        V: the speed limit in miles/hour 
'''
from constant import Constant
def calculate(h_app):
        # Divide by 3.6 to convert km/h to m/s 
        # MR stands for mass flow rate
        V_speed = Constant.V_speed/3.6
        MR_CA = V_speed * Constant.b * Constant.K * Constant.h_film * Constant.water_density
        MR_TP = V_speed * Constant.b * (1-Constant.K) * h_app * Constant.water_density
        MR_BW = 0.5 * V_speed * Constant.b *(h_app-(Constant.K*Constant.h_film)-((1-Constant.K) * h_app)) * Constant.water_density
        MR_SW = 0.5 * V_speed * Constant.b *(h_app-(Constant.K*Constant.h_film)-((1-Constant.K) * h_app)) * Constant.water_density

        # SD stands for spray density
        V = Constant.V
        SD_CA = (-2.69 * 10**(-5) * V + 2.43 * 10**(-3)) * MR_CA
        SD_TP = (1.16 * 10**(-5) * V - 5.25 * 10**(-5)) * MR_TP
        SD_BW = (2.67 * 10**(-5) * V - 4.71 * 10**(-4)) * MR_BW
        SD_SW = (1.65 * 10**(-5) * V - 3.99 * 10**(-4)) * MR_SW

        SD_total = SD_CA + SD_TP + SD_BW + SD_SW
        return SD_total
