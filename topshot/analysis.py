import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

def graph(momentId):
    df = pd.read_csv('transactions.csv')
    rslt_df = df.loc[df['momentId'] == momentId] 
    rslt_df["time"] = pd.to_datetime(rslt_df["time"])
    rslt_df = rslt_df.sort_values(by="time")

    rslt_df.plot.line(x="time", y="price")
    plt.show()

def graphInTimeRange(momentId, start_date, end_date):
    df = getDataframeRange(start_date, end_date)
    rslt_df = df.loc[df['momentId'] == momentId] 
    rslt_df["time"] = pd.to_datetime(rslt_df["time"])
    rslt_df = rslt_df.sort_values(by="time")

    rslt_df.plot.line(x="time", y="price")
    plt.show()

def getSalesOverPrice(price):
    df = pd.read_csv('transactions.csv')
    
    rslt_df = df.loc[df['price'] > price]
    rslt_df["time"] = pd.to_datetime(rslt_df["time"])
    rslt_df = rslt_df.sort_values(by="time")
    
    return rslt_df

def getAveragePrice():
    df = pd.read_csv('transactions.csv')
    
    return df['price'].mean()

# Format is YYYY-MM-DD
def getAveragePriceInTimeRange(start_date, end_date):
    df = getDataframeRange(start_date, end_date)
    return df['price'].mean()

def getNumberOfSalesInTimeRange(start_date, end_date):
    df = getDataframeRange(start_date, end_date)
    return len(df.index)

def percentageGrowthInTimeRange(momentId, start_date, end_date):
    df = getDataframeRange(start_date, end_date)
    rslt_df = df.loc[df['momentId'] == momentId] 
    rslt_df["time"] = pd.to_datetime(rslt_df["time"])
    rslt_df = rslt_df.sort_values(by="time")

    return (rslt_df.iloc[-1]['price'] - rslt_df.iloc[0]['price']) / rslt_df.iloc[0]['price']

def findLowPercentageGainMoments(start_date, end_date):
    df = pd.read_csv('moments.csv')
    for index, row in df.iterrows():
        growth = percentageGrowthInTimeRange(row['id'], start_date, end_date)
        if growth > 10:
            print(str(growth) + ' - ' + row['id'])

# UTILS
def getDataframeRange(start_date, end_date):
    df = pd.read_csv('transactions.csv')
    mask = (df['time'] > start_date) & (df['time'] <= end_date)

    return df.loc[mask]


graph('c561f66b-5bd8-451c-8686-156073c3fb69+de32d3fb-0e6a-447e-b42a-08bbf1607b7d')
