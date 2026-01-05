'''
This module provides the function that read the climate and traffic model data
long: longitude
lat: latitude
AADT: annual average daily traffic per lane
AADTT: annual average daily truck traffic per lane
t1: the number of days with snowfall
h_total: total snowfall during a winter season
t2: the number of days with snow melting
'''
import pandas as pd


class Calculation_load:
    def __init__(self, file_name):
        # Load traffic sheet and auto-detect number of rows
        traffic_df = pd.read_excel(file_name, sheet_name='traffic', usecols='A,B,D,E', skiprows=0)

        if not traffic_df.iloc[:, 0].isnull().any():
            self.long = traffic_df.iloc[:, 0].values
        if not traffic_df.iloc[:, 1].isnull().any():
            self.lat = traffic_df.iloc[:, 1].values
        if not traffic_df.iloc[:, 2].isnull().any():
            self.AADT = traffic_df.iloc[:, 2].values
        if not traffic_df.iloc[:, 3].isnull().any():
            self.AADTT = traffic_df.iloc[:, 3].values

        # Load t1 sheet and auto-detect number of rows
        t1_df = pd.read_excel(file_name, sheet_name='t1', usecols='B:CR', skiprows=0)
        if not t1_df.isnull().any().any():
            self.t1 = t1_df.values

        # Load htotal sheet and auto-detect number of rows
        htotal_df = pd.read_excel(file_name, sheet_name='htotal', usecols='B:CR', skiprows=0)
        if not htotal_df.isnull().any().any():
            self.h_total = htotal_df.values

        # Load t2 sheet and auto-detect number of rows
        t2_df = pd.read_excel(file_name, sheet_name='t2', usecols='B:CR', skiprows=0)
        if not t2_df.isnull().any().any():
            self.t2 = t2_df.values
