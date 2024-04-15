import numpy as np
import pandas as pd
import pandas as pd


class Calculation_load:

    def __init__(self, file_name):
        df1 = pd.read_excel(file_name, sheet_name='Sheet1', usecols='A,B,D,E', skiprows=0, nrows=1645)
        if not df1.iloc[:, 0].isnull().any():
            self.long = df1.iloc[:, 0].values
        if not df1.iloc[:, 1].isnull().any():
            self.lat = df1.iloc[:, 1].values
        if not df1.iloc[:, 2].isnull().any():
            self.AADT = df1.iloc[:, 2].values
        if not df1.iloc[:, 3].isnull().any():
            self.AADTT = df1.iloc[:, 3].values
        if not pd.read_excel(file_name, sheet_name='t1', usecols='B:BD', skiprows=0, nrows=1645).isnull().any().any():
            self.t1 = pd.read_excel(file_name, sheet_name='t1', usecols='B:BD', skiprows=0, nrows=1645).values
        if not pd.read_excel(file_name, sheet_name='htotal', usecols='B:BD', skiprows=0, nrows=1645).isnull().any().any():
            self.h_total = pd.read_excel(file_name, sheet_name='htotal', usecols='B:BD', skiprows=0, nrows=1645).values
        if not pd.read_excel(file_name, sheet_name='t2', usecols='B:BD', skiprows=0, nrows=1645).isnull().any().any():
            self.t2 = pd.read_excel(file_name, sheet_name='t2', usecols='B:BD', skiprows=0, nrows=1645).values

