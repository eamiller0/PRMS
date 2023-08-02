# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 17:12:22 2023

Retrieve data from tide gauge

Site IDs:
    Rigolets - 301001089442600
    East Pearl at RR Xing - 301141089320300
    
Services available from NWIS include:

instantaneous values (iv)
daily values (dv)
statistics (stat)
site info (site)
discharge peaks (peaks)
discharge measurements (measurements)
water quality samples (qwdata)


    
@author: Erin
"""
import pandas as pd
import numpy as np
import dataretrieval.nwis as nwis

# Specify parameters
site = '301141089320300'
startdt = '20040101'
enddt = '20230630'

# Get daily values (dv)
df = nwis.get_record(sites = site, service = 'dv', start = startdt, end = enddt)

# Get discharge measurements (measurements)
df2 = nwis.get_record(sites = site, service = 'measurements', start = startdt, end = enddt)

# Get discharge peaks (peaks)
df3 = nwis.get_record(sites = site, service = 'peaks', start = startdt, end = enddt)

# Get metadata for site
site_df = nwis.get_record(sites = site, service = 'site')


#








