import numpy as np
from calculation_load import Calculation_load
from constant import Constant


class Calculation_step1:

    def __init__(self, h_total, t1):
        self.h_total =  h_total
        self.t1 = t1
        self.M_app = np.zeros((1645, 95))

    def calculate(self):

        # % M_app, the quantity of deicing salts applied on a roadway per day during the winter season
        # % W_lane is the lane width in meter, take as 3.75
        # % Salt_application_rate is taken as 0.07
        self.M_app = Constant.salt_application_rate * self.h_total / (Constant.W_lane*self.t1);
        # print(self.M_app)


# last = Calculation_load()
# constant = constant()
# calculation_step1 = Calculation_step1(last.h_total, last.t1)
# calculation_step1.calculate()
# print(calculation_step1.M_app)
# print(calculation_step1.calculate())