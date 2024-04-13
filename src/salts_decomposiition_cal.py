import math
import numpy as np
from constant import Constant

def calculate(C_s_air):
    # % chloride on bridge surface
    # % d is the distance between road edge and bridge substructure, taken as
    # % 3.5m
    d = Constant.d
    C_spray = C_s_air * 0.015
    C_splash = C_s_air * 0.985
    results = C_spray * math.exp(-0.05*d) + C_splash * math.exp(-0.5*d)
    return results

