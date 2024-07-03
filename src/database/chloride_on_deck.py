'''
This module provides database for chloride on deck. It is
 based on a linear regression model that characterize the relationship between the 
 surface chloride concentration on bridge decks and two key factors: the annual snowfall amount (htotal) and the AADT
Output: results: the deposition of chloride on the deck of the bridge
Input:  h_total: total snowfall during a winter seasonConstant 
        AADT: annual average daily traffic per lane
'''

# TODO unit conversion

def deck_calculation(h_total, AADT):
    results = 0.11*h_total - 0.000189*AADT + 3.349
    return results
