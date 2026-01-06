'''
This module provides second step of the database generation.
Output: h_app: the thickness of melted water per day with snow melting
Input: h_total: total snowfall during a winter season
       t2: the number of days with snow melting
'''
import numpy as np


def calculate(h_total, t2):
    # calculate h_total water by dividing h_total by 12, according to Mingsai
    h_total_water = h_total / 12
    h_app = np.zeros_like(h_total_water, dtype=float)

    # mask where t2 > 0
    mask = t2 > 0

    # only compute where t2 > 0    
    # h_total is in centimeter but h_app need to be in meter, divide by 100 for unit conversion
    h_app[mask] = h_total_water[mask] / t2[mask] / 100

    return h_app
