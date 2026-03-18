import pandas as pd

df = pd.read_csv('crime_data.csv')

# Basic cleaning
df.dropna(subset=['DATE OCC', 'TIME OCC', 'Crm Cd Desc', 'AREA NAME'], inplace=True)
df.drop_duplicates(inplace=True)

# Parse date and time
df['DATE OCC'] = pd.to_datetime(df['DATE OCC'])
df['Hour'] = (df['TIME OCC'] // 100).astype(int)  # TIME OCC is in HHMM format
df['Month'] = df['DATE OCC'].dt.month
df['Year'] = df['DATE OCC'].dt.year
df['DayOfWeek'] = df['DATE OCC'].dt.dayofweek

print(f"Cleaned dataset: {df.shape[0]} records")
print(f"Date range: {df['DATE OCC'].min()} to {df['DATE OCC'].max()}")
print(f"Unique crime types: {df['Crm Cd Desc'].nunique()}")
df.to_csv('crime_clean.csv', index=False)
print("Saved to crime_clean.csv")