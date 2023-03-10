# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:28:44 2023

@author: BHANUKIRAN
"""

# Importing Necessary Libraries

import pandas as pd
from prophet import Prophet
import pickle

# preprocessing for fbprophet model

# Infosys

infosys_data = pd.read_csv('Data/infosys_data.csv')
infosys_data.set_index('Date', inplace=True)
infosys_data.index = pd.DatetimeIndex(infosys_data.index)
infosys_data = infosys_data.asfreq('b')
infosys_data.interpolate(method = 'linear', inplace = True)
infosys_data.reset_index(inplace = True)
infosys_data.rename({'Date':'ds','Close':'y'}, axis = 1, inplace = True)

# Reliance

reliance_data = pd.read_csv('Data/reliance_data.csv')
reliance_data.set_index('Date', inplace=True)
reliance_data.index = pd.DatetimeIndex(reliance_data.index)
reliance_data = reliance_data.asfreq('b')
reliance_data.interpolate(method = 'linear', inplace = True)
reliance_data.reset_index(inplace = True)
reliance_data.rename({'Date':'ds','Close':'y'}, axis = 1, inplace = True)

# Tata Motors

tatamotors_data = pd.read_csv('Data/tatamotors_data.csv')
tatamotors_data.set_index('Date', inplace=True)
tatamotors_data.index = pd.DatetimeIndex(tatamotors_data.index)
tatamotors_data = tatamotors_data.asfreq('b')
tatamotors_data.interpolate(method = 'linear', inplace = True)
tatamotors_data.reset_index(inplace = True)
tatamotors_data.rename({'Date':'ds','Close':'y'}, axis = 1, inplace = True)

# Wipro

wipro_data = pd.read_csv('Data/wipro_data.csv')
wipro_data.set_index('Date', inplace=True)
wipro_data.index = pd.DatetimeIndex(wipro_data.index)
wipro_data = wipro_data.asfreq('b')
wipro_data.interpolate(method = 'linear', inplace = True)
wipro_data.reset_index(inplace = True)
wipro_data.rename({'Date':'ds','Close':'y'}, axis = 1, inplace = True)

# Model Building

stocks = [infosys_data, reliance_data, tatamotors_data, wipro_data]
files = ['saved_models/infosys_model.sav', 'saved_models/reliance_model.sav', 
         'saved_models/tatamotors_model.sav', 'saved_models/wipro_model.sav']
x = 0

for i in stocks:
    
      
    # Model Building
    model = Prophet()
    model.fit(i)
    
    # Saving the Model
    file = files[x]
    pickle.dump(model, open(file, 'wb'))
    x = x+1