import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

# Method 4 (It's actually method 1 on the link provided)
for index, row in df.iterrows():
    total_cost_in_USD = row['local_price'] * row['dollar_ex']
    # mutiplication to calculate local price by exchnage rate to get cost in USD
    # but im not sure why some happen to be thousands of dollars
    print(f"{row['name']} Total Cost in USD: ${total_cost_in_USD}")

# Method 6 (It's actually method 3 on the link provided)
def calculate_total_cost(row):
   return f"{row['local_price'] * row['dollar_ex']:.2f}"
# returns the each countries cost in US dollars

df['Total Cost in USD'] = df.apply(calculate_total_cost, axis=1)
# sets up the table pretty
print(df[['name', 'Total Cost in USD']])
# gives headers to table
