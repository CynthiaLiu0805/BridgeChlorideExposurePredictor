import numpy as np
import pandas as pd
import pandas as pd


class Calculation_load:

    def __init__(self, file_name):
        df1 = pd.read_excel(file_name, sheet_name='Sheet1', usecols='A,B,D,E', skiprows=0, nrows=1645)

        self.long = df1.iloc[:, 0].values
        self.lat = df1.iloc[:, 1].values

        self.AADT = df1.iloc[:, 2].values
        self.AADTT = df1.iloc[:, 3].values
        self.t1 = pd.read_excel(file_name, sheet_name='t1', usecols='B:CR', skiprows=0, nrows=1645).values
        self.h_total = pd.read_excel(file_name, sheet_name='htotal', usecols='B:CR', skiprows=0, nrows=1645).values
        self.t2 = pd.read_excel(file_name, sheet_name='t2', usecols='B:CR', skiprows=0, nrows=1645).values

