# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 16:24:14 2022

@author: BHANUKIRAN
"""



import pandas as pd
import streamlit as st
from prophet.plot import plot_plotly
from plotly import graph_objs as go
import pickle



infosys_model = pickle.load(open("saved_models/infosys_model.sav", 'rb'))
reliance_model = pickle.load(open("saved_models/reliance_model.sav", 'rb'))
tatamotors_model = pickle.load(open("saved_models/tatamotors_model.sav", 'rb'))
wipro_model = pickle.load(open("saved_models/wipro_model.sav", 'rb'))

model_dict = {'Infosys': infosys_model,
              'Reliance': reliance_model,
              'Tatamotors': tatamotors_model,
              'Wipro': wipro_model}


infosys_data = pd.read_csv("Data/infosys_data.csv")
reliance_data = pd.read_csv("Data/reliance_data.csv")
tatamotors_data = pd.read_csv("Data/tatamotors_data.csv")
wipro_data = pd.read_csv("Data/wipro_data.csv")



data_dict = {'Infosys': infosys_data,
              'Reliance': reliance_data,
              'Tatamotors': tatamotors_data,
              'Wipro': wipro_data
              }






st.title('Stock Forecast App')

st.subheader('Select Stock for Forecasting')
selected_stock = st.selectbox('Stock', model_dict.keys())


@st.cache
def load_data(x):
    return x

data_load_state = st.text('Loading data...')
data = load_data(data_dict[selected_stock])
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data)


# Plot raw data
st.subheader('Time Series data with Rangeslider')

def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()



st.subheader('Select No. of months for Forecasting')

n_months = st.slider('Slide to select', 1, 12)
period = n_months * 30


def forecast(ticker):
    future = ticker.make_future_dataframe(periods = period)
    future_df = future[-291:]
    forecast = ticker.predict(future_df)
    
    
    st.subheader(f'Forecast plot for {n_months} months')
    fig1 = plot_plotly(ticker, forecast, xlabel = 'Time', ylabel = 'Predictions')
    st.plotly_chart(fig1)
    
    forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    forecast = forecast.rename(columns={"ds": "Date", "yhat": "Pred_Close", "yhat_lower" : "Pred_lower","yhat_upper":"Pred_upper"})
    forecast['Date'] = forecast['Date'].apply(lambda x: x.date())
    
    
    # Show and plot forecast
    st.subheader(f'Forecast data for {n_months} months')
    st.write(forecast.head(n_months*30))
    

forecast(model_dict[selected_stock])
