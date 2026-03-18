import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('crime_clean.csv')

# Crime by hour of day
hourly = df.groupby('Hour').size()
plt.figure(figsize=(12, 5))
sns.barplot(x=hourly.index, y=hourly.values, color='steelblue')
plt.title('LA Crime Frequency by Hour of Day (2020-Present)')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Incidents')
plt.tight_layout()
plt.savefig('crime_by_hour.png')
plt.close()
print("Saved crime_by_hour.png")

# Top 10 crime types
top_crimes = df['Crm Cd Desc'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_crimes.values, y=top_crimes.index, color='coral')
plt.title('Top 10 Crime Types in Los Angeles')
plt.xlabel('Number of Incidents')
plt.tight_layout()
plt.savefig('top_crimes.png')
plt.close()
print("Saved top_crimes.png")

# Crime by area
top_areas = df['AREA NAME'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_areas.values, y=top_areas.index, color='mediumseagreen')
plt.title('Top 10 High-Crime Areas in Los Angeles')
plt.xlabel('Number of Incidents')
plt.tight_layout()
plt.savefig('crime_by_area.png')
plt.close()
print("Saved crime_by_area.png")

print("\nKey Insights:")
print(f"Peak crime hour: {hourly.idxmax()}:00")
print(f"Most common crime: {df['Crm Cd Desc'].value_counts().index[0]}")
print(f"Highest crime area: {df['AREA NAME'].value_counts().index[0]}")