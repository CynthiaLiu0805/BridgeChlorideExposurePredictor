

import numpy as np
from calculation_load import Calculation_load


class Calculation_step2:
    def __init__(self, h_total, t2):
        self.h_total = h_total
        self.t2 = t2
        self.h_app = np.zeros((1645, 95))

    def calculate(self):
        # % h_app, thickness of melted water per day with snow melting
        # % h_total is in meter
        # print(self.t2)

        self.h_app = self.h_total / 12 /self.t2 /100

last = Calculation_load()
# constant = constant()
calculation_step1 = Calculation_step2(last.h_total, last.t2)
calculation_step1.calculate()
# print(calculation_step1.h_app)
