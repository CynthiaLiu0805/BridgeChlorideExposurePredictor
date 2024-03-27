import numpy as np
from constant import Constant
from calculation_load import Calculation_load
from calculation_step1 import Calculation_step1

from calculation_step2 import Calculation_step2
from calculation_step3 import Calculation_step3

from calculation_step4 import Calculation_step4


class Calculation_step5:
    
# % Loop through each column
# for i = 2:95
#    AADT(:,i) = AADT(:,i-1)+AADT(:,i-1)*(0.02);
#    AADTT(:,i) = AADTT(:,i-1)+AADTT(:,i-1)*(0.02);
# end
    def __init__(self, AADT, AADTT, SD_totalCl, t2):
        self.AADT = np.zeros((1645, 95))
        self.AADTT = np.zeros((1645, 95))
        self.SD_totalCl = SD_totalCl
        self.t2 = t2
        self.C_s_air_day = np.zeros((1645, 95))
        self.C_s_air = np.zeros((1645, 95))

        # because of the annual 2% increase in traffic volume, the AADT and AADTT are calculated as follows:
        for i in range(1, 95):
            self.AADT[:,0] = AADT
            self.AADTT[:,0] = AADTT
            self.AADT[:,i] = self.AADT[:,i-1] + self.AADT[:,i-1] * 0.02
            self.AADTT[:,i] = self.AADTT[:,i-1] + self.AADTT[:,i-1] * 0.02



    # because of the annual 2% increase in traffic volume, the AADT and AADTT are calculated as follows:
    # def update_AADT(self):
    #     for i in range(1, 95):
    #         self.AADT[:,i] = self.AADT[:,i-1] + self.AADT[:,i-1] * 0.02
    #         self.AADTT[:,i] = self.AADTT[:,i-1] + self.AADTT[:,i-1] * 0.02

    # % C_s_air: mass of chloride ions per unit air volume
    # % light-duty vehicles ratio can be taken as 6
    # % AADTT per lane
    def calculate(self):
        
        self.C_s_air_day = self.SD_totalCl / Constant.ldv_ratio * (self.AADT-self.AADTT) + self.SD_totalCl * self.AADTT
        self.C_s_air = self.C_s_air_day * self.t2

    



# load = Calculation_load()
# calculation_step1 = Calculation_step1(load.h_total, load.t1)
# calculation_step1.calculate()
# calculation_step2 = Calculation_step2(load.h_total, load.t2)
# calculation_step2.calculate()
# calculation_step3 = Calculation_step3(calculation_step2.h_app)
# calculation_step3.calculate()
# calculation_step4 = Calculation_step4(calculation_step3.h_app, calculation_step1.M_app, calculation_step3.SD_total)
# calculation_step4.calculate()
# calculation_step5 = Calculation_step5(load.AADT, load.AADTT, calculation_step4.SD_totalCl, load.t2)
# # calculation_step5.update_AADT()
# calculation_step5.calculate()
# print(calculation_step5.C_s_air)