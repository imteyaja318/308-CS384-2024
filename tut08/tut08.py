import pandas as pd

# Load the dataset
df = pd.read_csv('infy_stock.csv')

# Display the first 10 rows of the dataset
print(df.head(10))

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing Values:\n", missing_values)

# Handle missing values (if any)
df.fillna(method='ffill', inplace=True)  # Forward fill any missing values

#***************************************************************************

import matplotlib.pyplot as plt
import seaborn as sns

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Plot the closing price over time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Closing Price', color='b')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Closing Price Over Time')
plt.legend()
plt.show()


#**********************************************
#(b)
import matplotlib.pyplot as plt
import seaborn as sns

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Plot the closing price over time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Close'], label='Closing Price', color='b')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Closing Price Over Time')
plt.legend()
plt.show()

#*****************************************************

# Calculate daily return percentage
df['Daily Return %'] = ((df['Close'] - df['Open']) / df['Open']) * 100

# Display the first few daily return percentages
print(df[['Open', 'Close', 'Daily Return %']].head())


#*****************************************

# Calculate average and median of daily returns
average_return = df['Daily Return %'].mean()
median_return = df['Daily Return %'].median()

print(f"Average Daily Return: {average_return:.2f}%")
print(f"Median Daily Return: {median_return:.2f}%")

#***************************************************

# Calculate standard deviation of closing prices
std_close = df['Close'].std()
print(f"Standard Deviation of Closing Price: {std_close:.2f}")

#*******************************************

# Calculate 50-day and 200-day moving averages
df['50 MA'] = df['Close'].rolling(window=50).mean()
df['200 MA'] = df['Close'].rolling(window=200).mean()

# Plot the closing price and moving averages
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Close'], label='Closing Price', color='b')
plt.plot(df.index, df['50 MA'], label='50-Day Moving Average', color='r')
plt.plot(df.index, df['200 MA'], label='200-Day Moving Average', color='g')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Moving Averages')
plt.legend()
plt.show()

#****************************************

# Calculate rolling standard deviation (30-day window)
df['30 Day Volatility'] = df['Close'].rolling(window=30).std()

# Plot the volatility
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['30 Day Volatility'], label='30 Day Volatility', color='orange')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.title('30-Day Rolling Volatility')
plt.legend()
plt.show()

#**************************************************
# Identify bullish and bearish trends
df['Bullish'] = df['50 MA'] > df['200 MA']
df['Bearish'] = df['50 MA'] < df['200 MA']

# Plot the trends along with moving averages
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Close'], label='Closing Price', color='b')
plt.plot(df.index, df['50 MA'], label='50-Day Moving Average', color='r')
plt.plot(df.index, df['200 MA'], label='200-Day Moving Average', color='g')

# Highlight bullish trends
plt.fill_between(df.index, df['Close'].min(), df['Close'].max(), where=df['Bullish'], color='green', alpha=0.2, label='Bullish Trend')
# Highlight bearish trends
plt.fill_between(df.index, df['Close'].min(), df['Close'].max(), where=df['Bearish'], color='red', alpha=0.2, label='Bearish Trend')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Bullish and Bearish Trends')
plt.legend()
plt.show()

#**********************************************************