import numpy as np
from constant import Constant


def updateAADT(AADT):
        resultAADT = np.zeros((1645, 55))
        # because of the annual 2% increase in traffic volume, the AADT and AADTT are calculated as follows:
        for i in range(1, 55):
            resultAADT[:,0] = AADT
            resultAADT[:,i] = resultAADT[:,i-1] + resultAADT[:,i-1] * 0.02
        return resultAADT


def updateAADTT(AADTT):
        resultAADTT = np.zeros((1645, 55))
        # because of the annual 2% increase in traffic volume, the AADT and AADTT are calculated as follows:
        for i in range(1, 55):
            resultAADTT[:,0] = AADTT
            resultAADTT[:,i] = resultAADTT[:,i-1] + resultAADTT[:,i-1] * 0.02
        return resultAADTT


    # % C_s_air: mass of chloride ions per unit air volume
    # % light-duty vehicles ratio can be taken as 6
    # % AADTT per lane
def calculate(SD_totalCl, t2, AADT, AADTT):
    
    C_s_air_day = SD_totalCl / Constant.ldv_ratio * (AADT-AADTT) + SD_totalCl * AADTT
    C_s_air = C_s_air_day * t2
    return C_s_air

    
