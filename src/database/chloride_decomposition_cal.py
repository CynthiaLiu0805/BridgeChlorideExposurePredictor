'''
This module provides sixth, also the final step of the database generation. It is related to TM3 in SRS.
Output: results: the deposition of chloride on the surface of the bridge substructure
Input:  C_s_air: chloride ions sprayed and splashed by all vehicles in one winter season
Constant: 
        d: the distance between road edge and bridge substructure
'''
import math
import numpy as np
from constant import Constant
def calculate(C_s_air):
    d = Constant.d
    C_spray = C_s_air * 0.015
    C_splash = C_s_air * 0.985
    results = C_spray * math.exp(-0.05*d) + C_splash * math.exp(-0.5*d)
    return results