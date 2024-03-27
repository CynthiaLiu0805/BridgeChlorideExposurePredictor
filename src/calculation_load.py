import numpy as np
import pandas as pd
import pandas as pd

file_name = '1.xlsx'
df1 = pd.read_excel(file_name, sheet_name='Sheet1', usecols='A,B,D,E', skiprows=0, nrows=1645)


class Calculation_load:

    def __init__(self):
        self.long = df1.iloc[:, 0].values
        self.lat = df1.iloc[:, 1].values
        # self.AADT = np.zeros((1645, 95))
        # self.AADTT = np.zeros((1645, 95))

        self.AADT = df1.iloc[:, 2].values
        self.AADTT = df1.iloc[:, 3].values
        self.t1 = pd.read_excel(file_name, sheet_name='t1', usecols='B:CR', skiprows=0, nrows=1645).values
        self.h_total = pd.read_excel('1.xlsx', sheet_name='htotal', usecols='B:CR', skiprows=0, nrows=1645).values
        self.t2 = pd.read_excel('1.xlsx', sheet_name='t2', usecols='B:CR', skiprows=0, nrows=1645).values

    def get_h_total(self):
        return self.h_total
    # Read specific columns from 'Sheet1'

    #     # Assign columns to variables
    #     long = df1.iloc[:, 0].values
    # lat = df1.iloc[:, 1].values
    # AADT = df1.iloc[:, 2].values
    # AADTT = df1.iloc[:, 3].values

    # # Read specific ranges from other sheets
    # t1 = pd.read_excel('1.xlsx', sheet_name='t1', usecols='B:CR', skiprows=0, nrows=1645).values
    # h_total = pd.read_excel('1.xlsx', sheet_name='htotal', usecols='B:CR', skiprows=0, nrows=1645).values
    # t2 = pd.read_excel('1.xlsx', sheet_name='t2', usecols='B:CR', skiprows=0, nrows=1645).values

    # print(long[0], lat[0], AADT[0], AADTT[0], t1[0], h_total[0], t2[0])
    # print(long[1644], lat[1644], AADT[1644], AADTT[1644], t1[1644], h_total[1644], t2[1644])
        
# calculation_load = Calculation_load()
# print(calculation_load.long[0], calculation_load.lat[0], calculation_load.AADT[0], calculation_load.AADTT[0], calculation_load.t1[0], calculation_load.h_total[0], calculation_load.t2[0])