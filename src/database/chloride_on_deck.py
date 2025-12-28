'''
This module provides database for chloride on deck. It is
 based on a linear regression model that characterize the relationship between the
 surface chloride concentration on bridge decks and two key factors: the annual snowfall
 amount (htotal) and the AADT
Output: results: the deposition of chloride on the deck of the bridge
Input:  h_total: total snowfall during a winter seasonConstant
        AADT: annual average daily traffic per lane
'''


def deck_calculation(h_total, AADT):
    # Origin h_total is in cm, here it need to be in inches, divide by 2.54 for unit conversion
    # The unit of result is in lbs/yd^3 , multiply by 0.59 to convert lbs/yd^3 to kg/m^3
    results = (0.11*h_total/2.54 - 0.000189*AADT + 3.349)*0.59
    return results
