'''
This module provides first step of the database generation.
Output: M_app: the quantity of deicing salts applied on a roadway per day during the winter season
Input:  t1: the number of days with snowfall
        h_total: total snowfall during a winter season
Constant:
        W_lane: the lane width in meter
'''
from constant import Constant


def calculate(h_total, t1, salt_application_rate):
    M_app = salt_application_rate * h_total / (Constant.W_lane*t1)
    return M_app
