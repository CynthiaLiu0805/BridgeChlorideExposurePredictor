import unittest
import numpy as np
from calculation_load import Calculation_load

import calculation_step1
import calculation_step2

import calculation_step3

import calculation_step4
import calculation_step5
import calculation_step6

class TestCalculation(unittest.TestCase):
    def setUp(self):
        self.load = Calculation_load('1.xlsx')
        self.AADT = calculation_step5.updateAADT(self.load.AADT)
        self.AADTT = calculation_step5.updateAADTT(self.load.AADTT)
        self.M_app = calculation_step1.calculate(self.load.h_total, self.load.t1)
        self.h_app = calculation_step2.calculate(self.load.h_total, self.load.t2)
        self.SD_total = calculation_step3.calculate(self.h_app)
        self.SD_totalCl = calculation_step4.calculate(self.M_app, self.h_app, self.SD_total)

        self.C_s_air = calculation_step5.calculate(self.SD_totalCl, self.load.t2, self.AADT, self.AADTT)
        self.results = calculation_step6.calculate(self.C_s_air)

    def test_calculate_step1(self):
        expected_M_app = [0.0363145073858349, 0.0375421740531611, 0.0299470691769858, 0.0331207666034081, 0.0323051841884699]
        np.testing.assert_almost_equal(self.M_app[:5,0], expected_M_app)

    def test_calculate2(self):
        expected_h_app = [0.00238450596609997, 0.00210023525470920, 0.00210182981793956, 0.00287288260788614, 0.00284220860781388]
        np.testing.assert_almost_equal(self.h_app[5:10,1], expected_h_app)

    def test_calculate3(self):
        expected_SD_total = [0.0150332110813748, 0.0142798549589450, 0.0130397006930074, 0.0104225247001255, 0.0125935080686887]
        np.testing.assert_almost_equal(self.SD_total[9:14, 2], expected_SD_total)

    def test_calculate4(self):
        expected_SD_totalCl = [0.000290316777022655, 0.000300172629825103, 0.000238811750170985, 0.000264442784673519, 0.000258105568914589]
        np.testing.assert_almost_equal(self.SD_totalCl[:5, 0], expected_SD_totalCl)

    def test_calculate5(self):
        expected_C_s_air = [4.73051178779328, 3.96981034531171, 3.51064220140197, 2.95976102415515, 3.29189034747470]
        np.testing.assert_almost_equal(self.C_s_air[5:10, 1], expected_C_s_air)

    def test_calculate6(self):
        expected_results = [0.796928663149077, 0.660801640766927, 0.552286875781850, 0.616013631554310, 0.628572271378117]
        np.testing.assert_almost_equal(self.results[10:15, 2], expected_results)  


if __name__ == '__main__':
    unittest.main()