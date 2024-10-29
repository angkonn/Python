!pip install pandas matplotlib seaborn
import pandas as pd
data = pd.read_csv("country_wise_latest.csv")  
data
# Looking at the first few rows
print(data.head())

# Getting info on data types and missing values
print(data.info())

# Looking at column names
print(data.columns)

# Checking for missing values
print(data.isnull().sum())

# Dropping rows with missing values
data = data.dropna()

print(data.columns)

# Summary of cases by WHO Region
region_summary = data.groupby('WHO Region')[['Confirmed', 'Deaths', 'Recovered']].sum()
print(region_summary)

# Plot total confirmed cases by WHO Region
region_summary['Confirmed'].plot(kind='bar', figsize=(10,5), title="Total Confirmed Cases by WHO Region")
plt.xlabel("WHO Region")
plt.ylabel("Total Confirmed Cases")
plt.show()


# Top 10 countries with highest death rate per 100 cases
top_death_rate = data.nlargest(10, 'Deaths / 100 Cases')[['Country/Region', 'Deaths / 100 Cases']]
print(top_death_rate)

# Plot recovery rates
plt.figure(figsize=(10, 5))
sns.barplot(x='Country/Region', y='Recovered / 100 Cases', data=data.nlargest(10, 'Recovered / 100 Cases'))
plt.title("Top 10 Countries by Recovery Rate") 
plt.xticks(rotation=90)
plt.show()

# Countries with highest 1 week % increase
top_week_increase = data.nlargest(10, '1 week % increase')[['Country/Region', '1 week % increase']]
print(top_week_increase)

# Plot
sns.barplot(x='Country/Region', y='1 week % increase', data=top_week_increase)
plt.xticks(rotation=90)
plt.title("Top 10 Countries by Weekly % Increase in Cases")
plt.show()


# New cases, deaths, and recoveries for a few sample countries
sample_countries = data[data['Country/Region'].isin(['Afghanistan', 'Albania', 'Algeria', 'Andorra'])]
plt.figure(figsize=(12, 8))

sns.barplot(x='Country/Region', y='New cases', data=sample_countries, color='blue', label='New Cases')
sns.barplot(x='Country/Region', y='New deaths', data=sample_countries, color='red', label='New Deaths')
sns.barplot(x='Country/Region', y='New recovered', data=sample_countries, color='green', label='New Recovered')

plt.legend()
plt.xlabel("Country")
plt.ylabel("Count")
plt.title("New COVID-19 Cases, Deaths, and Recoveries by Country")
plt.xticks(rotation=45)
plt.show()


# Top 10 countries with most active cases
top_active_cases = data.nlargest(10, 'Active')[['Country/Region', 'Active']]
print(top_active_cases)

# Plot active cases
sns.barplot(x='Country/Region', y='Active', data=top_active_cases)
plt.xticks(rotation=90)
plt.title("Top 10 Countries by Active COVID-19 Cases")
plt.show()




