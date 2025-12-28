'''
This module includes the test for checking the empty values in the climate and traffic data.
It is checking if there are any null values in the specific column of the DataFrame
'''
import unittest
import pandas as pd
from pathlib import Path

# Get the directory of the current test file (so works locally and for CI)
TEST_FILE_DIR = Path(__file__).parent

# Construct the path to the data file
data_file_path = TEST_FILE_DIR / '../../data/data.xlsx'


class TestCalculation(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_excel(data_file_path, sheet_name='traffic', usecols='A,B,D,E',
                                skiprows=0)
        self.t1 = pd.read_excel(data_file_path, sheet_name='t1', usecols='B:BD', skiprows=0)
        self.h_total = pd.read_excel(data_file_path, sheet_name='htotal', usecols='B:BD',
                                     skiprows=0)
        self.t2 = pd.read_excel(data_file_path, sheet_name='t2', usecols='B:BD', skiprows=0)

    def test_longitude(self):
        self.assertFalse(self.df.iloc[:, 0].isnull().any())

    def test_latitude(self):
        self.assertFalse(self.df.iloc[:, 1].isnull().any())

    def test_AADT(self):
        self.assertFalse(self.df.iloc[:, 2].isnull().any())

    def test_AADTT(self):
        self.assertFalse(self.df.iloc[:, 3].isnull().any())

    def test_t1(self):
        self.assertFalse(self.t1.isnull().any().any())

    def test_h_total(self):
        self.assertFalse(self.h_total.isnull().any().any())

    def test_t2(self):
        self.assertFalse(self.t2.isnull().any().any())


if __name__ == '__main__':
    unittest.main()
