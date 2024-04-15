'''
This module provides first step of the database generation. It is related to DD1 in SRS.
Output: M_app: the quantity of deicing salts applied on a roadway per day during the winter season
Input:  t1: the number of days with snowfall
        h_total: total snowfall during a winter season
Constant:
        W_lane: the lane width in meter
        Salt_application_rate: salt application rate
'''
from constant import Constant
def calculate(h_total, t1):
    M_app = Constant.salt_application_rate * h_total / (Constant.W_lane*t1)
    return M_app