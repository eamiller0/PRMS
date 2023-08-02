# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 19:05:30 2023

Plots monthly averaged water data from USGS

@author: Erin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import dataretrieval.nwis as nwis
import warnings

#Variables
site = '02492700'
startdt = '2016-10-05'
enddt = '2023-06-30'

#Ignore "FutureWarnings" while executing the following code
warnings.filterwarnings("ignore")

# Get daily values (dv)
df = nwis.get_record(sites = site, service = 'dv', start = startdt, end = enddt)

# Get metadata for site
site_df = nwis.get_record(sites = site, service = 'site')

#Drop column named 00065_Mean_cd
df = df.drop(['00065_Mean_cd'], axis=1)

#Fix names of columns and index
df.rename(columns={'00065_Mean': 'Daily Mean', 'site_no': 'Site #'}, inplace=True)
df.index.names = ['Date']

#group the rows by month
monthly_df = df.resample('M').mean()

#Every year
years = mdates.YearLocator()

#Every month
months = mdates.MonthLocator()

#Format for year
years_fmt = mdates.DateFormatter('%Y')

#Convert dataframe to an np.array
data = monthly_df.to_records()

fig, ax = plt.subplots()
ax.plot('Date', 'Daily Mean', data=data, label='Monthly Mean')

#Format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(years_fmt)
ax.xaxis.set_minor_locator(months)

ax.grid(True)
  
plt.title('Gauge Height Monthly Average - Pearl River (02492700)')
plt.xlabel('Year')
plt.ylabel('Gauge Height (Feet)')
plt.legend()

plt.savefig('month_data_pearlRiver', dpi=600)
plt.show()
