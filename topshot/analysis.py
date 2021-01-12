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


graph('7b797690-5b53-45a7-b972-bd2d5152654a+a53dc13f-3b6a-40f0-816d-5f222b239296')
