'''
This module provides second step of the database generation.
Output: h_app: the thickness of melted water per day with snow melting
Input: h_total: total snowfall during a winter season
       t2: the number of days with snow melting
'''
def calculate(h_total, t2):
    # calculate h_total water by dividing h_total by 12, according to Mingsai
    # h_total is in centimeter but h_app need to be in meter, divide by 100 for unit conversion
    h_total_water = h_total /12
    h_app = h_total_water / t2 /100
    return h_app