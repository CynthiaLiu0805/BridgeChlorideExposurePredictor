'''
This module provides fourth step of the database generation.
Output: SD_totalCl: the chloride ions sprayed and splashed by one truck
Input:
        M_app: the quantity of deicing salts applied on a roadway per day during the winter season
        h_app: the thickness of melted water per day with snow melting
        SD_total: the water sprayed and splashed by one truck
Constant:
        water_density: water density
        chloride_ratio: molar mass ratio of chloride ions over deicing salts
'''
from constant import Constant


def calculate(M_app, h_app, SD_total):
    # ratio of the mass of salt over the mass of water per unit area of road
    salt_to_water_ratio = M_app / (h_app * Constant.water_density)
    SD_totalCl = SD_total * salt_to_water_ratio * Constant.chloride_ratio
    return SD_totalCl
