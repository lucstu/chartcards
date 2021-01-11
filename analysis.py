import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

df = pd.read_csv('transactions.csv')
rslt_df = df.loc[df['momentId'] == 'e2c09c0f-e04b-45db-9f5f-7cd0e6c5ed2b'] 
rslt_df[::-1]

print(rslt_df)

# rslt_df.plot.line(x="time", y="price")
# plt.show()