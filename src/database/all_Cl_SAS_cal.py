"""
This module provides fifth step of the database generation.
Output: C_s_air: chloride ions sprayed and splashed by all vehicles in one
        winter season
Input:  SD_totalCl: the chloride ions sprayed and splashed by one truck
        t2: the number of days with snow melting
        AADT: annual average daily traffic per lane
        AADTT: annual average daily truck traffic per lane
Constant:
        ldv_ratio: ratio of chloride ions sprayed and splashed by trucks to
        light duty vehicles
"""

import numpy as np
from constant import Constant


# Because of the annual 2% increase in traffic volume, the AADT and AADTT are
# calculated as follows:
def updateAADT(AADT):
    resultAADT = np.zeros((1645, 95))
    for i in range(1, 95):
        resultAADT[:, 0] = AADT
        resultAADT[:, i] = resultAADT[:, i - 1] + resultAADT[:, i - 1] * 0.02
    return resultAADT


def updateAADTT(AADTT):
    resultAADTT = np.zeros((1645, 95))
    for i in range(1, 95):
        resultAADTT[:, 0] = AADTT
        resultAADTT[:, i] = resultAADTT[:, i - 1] + resultAADTT[:, i - 1] * 0.02
    return resultAADTT


def calculate(SD_totalCl, t2, AADT, AADTT):

    C_s_air = (
        SD_totalCl / Constant.ldv_ratio * (AADT - AADTT) + SD_totalCl * AADTT
    ) * t2
    return C_s_air
