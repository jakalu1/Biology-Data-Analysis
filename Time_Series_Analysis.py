#Time Series analysis creator

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Assuming your data is stored in a CSV file named 'data.csv'
df = pd.read_csv('date_metadata.csv')


df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)


plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], marker='o', linestyle='-')
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()


# Assuming you want to predict future values for the next 30 days
future_dates = pd.date_range(start=df.index[-1], periods=30, freq='D')
future_dates_df = pd.DataFrame(index=future_dates)

model = LinearRegression()
model.fit(df.index.values.reshape(-1, 1), df['Value'])
future_values = model.predict(future_dates_df.index.values.reshape(-1, 1))

plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Value'], marker='o', linestyle='-', label='Actual Data')
plt.plot(future_dates, future_values, marker='o', linestyle='--', color='red', label='Predicted Data')
plt.title('Predictive Analysis')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
