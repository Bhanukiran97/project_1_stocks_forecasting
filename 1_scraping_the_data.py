# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 18:55:33 2023

@author: BHANUKIRAN
"""

# Importing Necessary Libraries

import nsepy
from datetime import date

# Extracting Data from NSE

# Infosys

infosys_data = nsepy.get_history(symbol = "INFY", start = date(2013,1,1), end = date.today())
infosys_data.drop(['Symbol','Series','Prev Close','Open','High','Low','Last','VWAP','Volume',
                   'Turnover','Trades','Deliverable Volume','%Deliverble'], axis = 1, inplace = True)
infosys_data.to_csv('Data/infosys_data.csv')

# Reliance

reliance_data = nsepy.get_history(symbol = "RELIANCE", start = date(2013,1,1), end = date.today())
reliance_data.drop(['Symbol','Series','Prev Close','Open','High','Low','Last','VWAP','Volume',
                   'Turnover','Trades','Deliverable Volume','%Deliverble'], axis = 1, inplace = True)
reliance_data.to_csv('Data/reliance_data.csv')

# Tata Motors

tatamotors_data = nsepy.get_history(symbol = "TATAMOTORS", start = date(2013,1,1), end = date.today())
tatamotors_data.drop(['Symbol','Series','Prev Close','Open','High','Low','Last','VWAP','Volume',
                   'Turnover','Trades','Deliverable Volume','%Deliverble'], axis = 1, inplace = True)
tatamotors_data.to_csv('Data/tatamotors_data.csv')

# Wipro

wipro_data = nsepy.get_history(symbol = "WIPRO", start = date(2013,1,1), end = date.today())
wipro_data.drop(['Symbol','Series','Prev Close','Open','High','Low','Last','VWAP','Volume',
                   'Turnover','Trades','Deliverable Volume','%Deliverble'], axis = 1, inplace = True)
wipro_data.to_csv('Data/wipro_data.csv')
