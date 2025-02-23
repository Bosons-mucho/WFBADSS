import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
#import yfinance as yf
#import mplfinance as mpf
#import ta
#import statsmodels
import datetime
import scipy
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

csv_file = load_data('market_data.csv')

df = csv_file
df['Intrinsic Value'] = (df['Undl Price'] - df['Strike']).apply(lambda x: max(x, 0))
df = df.rename(columns={'Bid Size ':'Bid Size', 'Ask Size ':'Ask Size'})
print(df.head())

df['Bid Intrinsic Exposure'] = df['Intrinsic Value'] * df['Bid Size']
df['Ask Intrinsic Exposure'] = df['Intrinsic Value'] * df['Ask Size']

# total_bid_exposure = df['Bid Intrinsic Exposure'].sum()
# total_ask_exposure = df['Ask Intrinsic Exposure'].sum()

# print(f'Total Bid Intrinsic Exposure: {total_bid_exposure}')
# print(f'Total Ask Intrinsic Exposure: {total_ask_exposure}')

df.head()

days = list(df['Date'].value_counts(sort=False).index)