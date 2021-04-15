from pandas_datareader import data as pdr
from datetime import date
import yfinance as yf
yf.pdr_override()
import pandas as pd
from yahoo_fin.stock_info import get_data

#
# # Tickers list
# # We can add and delete any ticker from the list to get desired ticker live data
# ticker_list=['DJIA', 'DOW', 'LB', 'EXPE', 'PXD', 'MCHP', 'CRM', 'JEC' , 'NRG', 'HFC', 'NOW']
# today = date.today()
# # We can get data by our choice by giving days bracket
# start_date= '2017–01–01'
# end_date='2019–11–30'
# files=[]
# def getData(ticker):
#     print (ticker)
#     data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
#     dataname = ticker+'_'+str(today)
#     files.append(dataname)
#     SaveData(data, dataname)
# # Create a data folder in your current dir.
# def SaveData(df, filename):
#     df.to_csv('./data/'+filename+'.csv')
# #This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
#     for tik in ticker_list:
#         getData(tik)
#     for i in range(0,11):
#         df1= pd.read_csv('./data/'+ str(files[i])+'.csv')
#         print (df1.head())
#



amazon_weekly= get_data("amzn", start_date="12/04/2018", end_date="12/04/2021", index_as_date = True, interval="1wk")
print(amazon_weekly)