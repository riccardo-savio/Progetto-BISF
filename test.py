import pandas as pd
import matplotlib.pyplot as plt

QCOM = pd.read_csv('QCOM.csv')
NVDA = pd.read_csv('NVDA.csv')
UNH = pd.read_csv('UNH.csv')
SO = pd.read_csv('SO.csv')
NEE = pd.read_csv('NEE.csv')
LLY = pd.read_csv('LLY.csv')

stocks = {'QCOM': QCOM, 'NVDA': NVDA, 'UNH': UNH, 'SO': SO, 'NEE': NEE, 'LLY': LLY}


""" df_adj_close = pd.DataFrame({'SP500': SP500['Adj Close'], 'NVDA': NVDA['Adj Close'], 'UNH': UNH['Adj Close'], 'SO': SO['Adj Close'], 'NEE': NEE['Adj Close'], 'LLY': LLY['Adj Close']})
df_adj_close.plot() """

for i, (key, value) in enumerate(stocks.items()):
    #set Date as index

    fig, ax = plt.subplots( nrows=2, ncols=1, sharex=True, sharey=False, height_ratios=[5, 1])
    value['Date'] = pd.to_datetime(value['Date'])
    value[["Date","Open","High","Low","Close","Adj Close"]].plot(ax=ax[0], x='Date')
    ax[0].set_ylabel('Prezzo')
    ax[0].set_xlabel('Data')

    value[['Date', 'Volume']].plot(ax=ax[1], x='Date')
    ax[1].set_ylabel('Volume')
    ax[1].set_xlabel('Data')
    plt.title(key)
    plt.grid()
    plt.tight_layout()
    plt.savefig(f'./images/{key}.png')