# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 02:14:33 2023

Plot turbidity data

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
import dataretrieval.nwis as nwis
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os

#Get and plot turbidity data
# Specify parameters
site = '301141089320300'
startdt = '2005-01-01'
enddt = '2023-06-30'

# Get daily values (dv)
df = nwis.get_record(sites = site, service = 'dv', start = startdt)

#Create new dataframe with only the columns we want (for coastal sites)
turb1_df = df[['site_no', '63680_Maximum', '63680_Minimum', '63680_Mean']].copy()

#Fix names of axes
turb1_df.rename(columns={'site_no':'Site #', '63680_Maximum':'Max Turbidity', '63680_Minimum': 'Min Turbidity', 
                    '63680_Mean':'Mean Turbidity'}, inplace=True)
turb1_df.index.names = ['Date']

#Plot data
turb1_df.plot()

#Every year
years = mdates.YearLocator()

#Every month
months = mdates.MonthLocator()

#Format for year
years_fmt = mdates.DateFormatter('%Y')

#Format the ticks
#ax.xaxis.set_major_locator(years)
#ax.xaxis.set_major_formatter(years_fmt)
#ax.xaxis.set_minor_locator(months)
#plt.savefig('month_turbidity_eastPearl', dpi=600)

plt.show()
