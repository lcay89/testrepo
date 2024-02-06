import yfinance as yf
import pandas as pd
amd = yf.Ticker('AAPL')
import json
with open('amd.json') as json_file:
	amd_info = json.load(json_file)
amd_share = amd.history(period='max')
# amd_share = amd.history(start='1972-09-27')
# amd_share.reset_index(inplace=True)
print(amd_share)