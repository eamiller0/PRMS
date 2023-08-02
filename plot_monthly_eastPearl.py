# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 00:47:49 2023

Plot East Pearl data

Rigolets at Hwy 90 near Slidell, LA - 301001089442600
East Pearl River at CsX railroad near Clairborne, MS - 301141089320300
Pearl River at I-10 near Slidell, LA - 02492700

Dates available: 2016-10-05 thru 2023-02-13 (as of 21Jul23) for Pearl River
                 2004-02-01 thru 2023-04-01 (as of 21Jul23) for Rigolets
                 2001-08-23 thru 2023-05-15 (as of 21Jul23) for East Pearl

service: string
        - 'iv' : instantaneous data
        - 'dv' : daily mean data
        - 'qwdata' : discrete samples
        - 'site' : site description
        - 'measurements' : discharge measurements
        - 'peaks': discharge peaks
        - 'gwlevels': groundwater levels
        - 'pmcodes': get parameter codes
        - 'water_use': get water use data
        - 'ratings': get rating table
        - 'stat': get statistics

@author: Erin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import dataretrieval.nwis as nwis
import os

# Specify parameters
site = '301141089320300'
startdt = '2001-01-01'
enddt = '2023-06-30'

# Get daily values (dv)
df = nwis.get_record(sites = site, service = 'dv', start = startdt)

#Create new dataframe with only the columns we want (for coastal sites)
df2 = df[['site_no', '00010_Mean',  '00060_Maximum', '00060_Minimum', '00060_Mean','00065_Tidal High-High',
          '00065_Tidal Low-Low', '00480_Mean']].copy()

#Fix names of axes
df2.rename(columns={'site_no':'Site #', '00010_Mean':'Mean Water Temp', '00060_Maximum':'Max Discharge',
                    '00060_Minimum':'Min Discharge', '00060_Mean':'Mean Discharge', '00065_Tidal High-High':'High Tide Gauge Ht',
                    '00065_Tidal Low-Low':'Low Tide Gauge Ht', '00480_Mean':'Mean Salinity'}, inplace=True)
df2.index.names = ['Date']

#group the rows by month
monthly = df2.resample('M').mean()

#A few functions for plotting

#Every year
years = mdates.YearLocator()

#Every month
months = mdates.MonthLocator()

#Format for year
years_fmt = mdates.DateFormatter('%Y')

#Split data into sets by parameter
sal_df = monthly['Mean Salinity'].copy()
dsch_df = monthly[['Max Discharge', 'Min Discharge', 'Mean Discharge']].copy()
ght_df = monthly[['High Tide Gauge Ht', 'Low Tide Gauge Ht']].copy()
temp_df = monthly['Mean Water Temp'].copy()

#Plot data
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, sharex=True)
fig.suptitle('Monthly Water Data - East Pearl', fontsize=16)

#Water temp subplot
ax1.plot(temp_df, linewidth=1)
ax1.set_ylabel('Temp (C)')
ax1.set_title('Water Temp', fontsize=12)
ax1.legend(['Mean Water Temp'], loc='lower right')
ax1.grid()

#Salinity subplot (Mean)
ax2.plot(sal_df, linewidth=1)
ax2.set_ylabel('Salinity (ppt)')
ax2.set_title('Salinity', fontsize=12)
ax2.legend(['Mean Salinity'], loc='lower right')
ax2.grid()

#Gauge height subplot (High Tide, Low Tide)
ax3.plot(ght_df, linewidth=1)
ax3.set_ylabel('Height (ft)')
ax3.set_title('Gauge Height', fontsize=12)
ax3.legend(['High Tide Gauge Ht', 'Low Tide Gauge Ht'], loc='lower right')
ax3.grid()

#Discharge subplot (Max, Min, Mean)
ax4.plot(dsch_df, linewidth=1)
ax4.set_ylabel('ft^3/s')
ax4.set_title('Discharge', fontsize=12)
ax4.legend(['Max Discharge', 'Min Discharge', 'Mean Discharge'], loc='lower right')
ax4.grid()

#Format the ticks
#ax3.xaxis.set_major_locator(years)
#ax3.xaxis.set_major_formatter(years_fmt)
ax4.xaxis.set_minor_locator(years)

fig.supxlabel('Year')
plt.savefig('month_data_eastPearl', dpi=600)

plt.show()
