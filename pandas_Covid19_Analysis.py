"""Mini Project final - numpy and pandas"""

# # ==========================================================
# # MINI PROJECT — COVID-19 Trend & Vaccination Analysis
# # ==========================================================

# PROJECT EXPLANATION
# ==========================================================

# In this project, students will analyze a COVID-19 dataset
# containing information about:

# - Daily cases
# - Deaths
# - Vaccinations
# - Testing
# - Hospitalizations
# - Growth rates
# - Pandemic waves
# - Government policies

# The main objective is to understand:

# - How COVID spread across countries
# - How vaccination affected cases and deaths
# - Which countries were highly affected
# - Which pandemic waves were more dangerous
# - How trends changed over time

# Students will use only:
# - Pandas
# - NumPy

# to clean, process, and analyze the dataset.

# ==========================================================
# TASK 1 — DATA UNDERSTANDING
# ==========================================================

# Explanation:
# Students first explore the dataset structure.

# They must understand:
# - how many rows and columns exist
# - what each column represents
# - which columns are numeric
# - which columns are categorical
# - whether missing values exist

# This step helps students become familiar with
# real-world datasets before analysis begins.



# ==========================================================
# TASK 2 — MISSING VALUE HANDLING
# ==========================================================

# Explanation:
# Real-world datasets usually contain incomplete data.

# Some rows may contain:
# - NaN values
# - missing numbers
# - empty strings

# Students must:
# - identify missing values
# - clean the dataset
# - replace missing numeric values using mean
# - replace categorical values using mode

# This task teaches data preprocessing.

# ==========================================================
# TASK 3 — COUNTRY-WISE ANALYSIS
# ==========================================================

# Explanation:
# Students analyze COVID statistics country by country.

# They compare:
# - total cases
# - total deaths
# - vaccination rates
# - recovery counts

# Students identify:
# - most affected countries
# - safest countries
# - highly vaccinated countries

# This task teaches grouping and comparison analysis.

# ==========================================================
# TASK 4 — GROWTH RATE ANALYSIS
# ==========================================================

# Explanation:
# The dataset contains growth rate columns such as:

# - cases_growth_rate_7d
# - deaths_growth_rate_7d

# Students analyze:
# - how fast cases increased
# - how fast deaths increased
# - periods where spread became dangerous

# This task helps students understand trend analysis.

# ==========================================================
# TASK 5 — WAVE ANALYSIS
# ==========================================================

# Explanation:
# COVID spread happened in multiple waves.

# Dataset contains:
# - wave_name
# - wave_phase

# Students analyze:
# - which wave had highest deaths
# - which wave had highest positivity rate
# - which phase was most dangerous

# This task teaches time-based comparison analysis.

# ==========================================================
# TASK 6 — VACCINATION IMPACT ANALYSIS
# ==========================================================

# Explanation:
# Students analyze whether vaccination reduced:

# - new cases
# - deaths
# - positivity rate

# Students compare:
# - countries with high vaccination
# - countries with low vaccination

# Goal:
# Understand effectiveness of vaccination programs.

# ==========================================================
# TASK 7 — MOVING AVERAGE ANALYSIS
# ==========================================================

# Explanation:
# Dataset contains moving average columns such as:

# - new_cases_ma7d
# - new_cases_ma14d
# - new_cases_ma30d

# Students analyze:
# - short-term trends
# - long-term trends
# - sudden spikes
# - stable periods

# This task teaches smoothing and trend observation.

# ==========================================================
# TASK 8 — CORRELATION ANALYSIS
# ==========================================================

# Explanation:
# Students find relationships between features.

# Examples:
# - vaccination vs deaths
# - mobility vs cases
# - positivity rate vs hospitalizations

# Students identify:
# - positive correlations
# - negative correlations
# - strongest relationships

# This task teaches statistical relationship analysis.

# ==========================================================
# TASK 9 — HIGH RISK DETECTION
# ==========================================================

# Explanation:
# Students identify dangerous countries using:

# - positivity rate
# - ICU admissions
# - hospitalization counts
# - Rt values

# Countries can be classified into:
# - Low Risk
# - Medium Risk
# - High Risk

# This task teaches rule-based classification logic.

# ==========================================================
# TASK 10 — FINAL INSIGHT GENERATION
# ==========================================================

# Explanation:
# Students summarize final findings from dataset.

# Examples:
# - Which country handled COVID best?
# - Which wave was most dangerous?
# - Did vaccines reduce deaths?
# - Which factor increased spread most?

# This task teaches analytical thinking and
# data interpretation.

# ==========================================================
# END OF PROJECT
# ==========================================================

# Real Projects Answers


import numpy as np
import pandas as pd

# Create a DataFrame from the CSV file

df = pd.read_csv('/content/drive/MyDrive/covid_processed.csv')
# print(df)

# TASK 1 — DATA UNDERSTANDING

# print(df.head())
# print(df.info())
# print(df.shape)
# print(df.describe())

# TASK 2 — MISSING VALUE HANDLING

df['target_new_cases_14d'] = df['target_new_cases_14d'].fillna(df['target_new_cases_14d'].mean())
df['target_new_deaths_14d'] = df['target_new_deaths_14d'].fillna(df['target_new_deaths_14d'].mean())
df['target_rt_7d'] = df['target_rt_7d'].fillna(df['target_rt_7d'].mean())
df['target_trend_7d'] = df['target_trend_7d'].fillna(df['target_trend_7d'].mean())
df['target_in_wave'] = df['target_in_wave'].fillna(df['target_in_wave'].mean())
df['policy_effectiveness'] = df['policy_effectiveness'].fillna(df['policy_effectiveness'].mean())
df['cases_growth_rate_7d'] = df['cases_growth_rate_7d'].fillna(df['cases_growth_rate_7d'].mean())
df['deaths_growth_rate_7d'] = df['deaths_growth_rate_7d'].fillna(df['deaths_growth_rate_7d'].mean())
df['rt_approx'] = df['rt_approx'].fillna(df['rt_approx'].mean())
df['vax_growth_rate_7d'] = df['vax_growth_rate_7d'].fillna(df['vax_growth_rate_7d'].mean())

df['new_deaths_lag28d'] = df['new_deaths_lag28d'].fillna(df['new_deaths_lag28d'].mean())
df['positivity_rate_pct_lag28d'] = df['positivity_rate_pct_lag28d'].fillna(df['positivity_rate_pct_lag28d'].mean())
df['new_cases_lag28d'] = df['new_cases_lag28d'].fillna(df['new_cases_lag28d'].mean())
df['new_cases_lag21d'] = df['new_cases_lag21d'].fillna(df['new_cases_lag21d'].mean())
df['positivity_rate_pct_lag21d'] = df['positivity_rate_pct_lag21d'].fillna(df['positivity_rate_pct_lag21d'].mean())

df['new_deaths_lag21d'] = df['new_deaths_lag21d'].fillna(df['new_deaths_lag21d'].mean())
df['positivity_rate_pct_lag14d'] = df['positivity_rate_pct_lag14d'].fillna(df['positivity_rate_pct_lag14d'].mean())
df['new_cases_lag14d'] = df['new_cases_lag14d'].fillna(df['new_cases_lag14d'].mean())
df['new_deaths_lag14d'] = df['new_deaths_lag14d'].fillna(df['new_deaths_lag14d'].mean())
df['new_cases_lag7d'] = df['new_cases_lag7d'].fillna(df['new_cases_lag7d'].mean())
df['new_deaths_lag7d'] = df['new_deaths_lag7d'].fillna(df['new_deaths_lag7d'].mean())
df['positivity_rate_pct_lag7d'] = df['positivity_rate_pct_lag7d'].fillna(df['positivity_rate_pct_lag7d'].mean())

df['cases_acceleration_7d'] = df['cases_acceleration_7d'].fillna(df['cases_acceleration_7d'].mean())
df['deaths_acceleration_7d'] = df['deaths_acceleration_7d'].fillna(df['deaths_acceleration_7d'].mean())
df['target_new_cases_7d'] = df['target_new_cases_7d'].fillna(df['target_new_cases_7d'].mean())

df['wave_name'] = df['wave_name'].replace('none', 'Unclassified')
df['wave_phase'] = df['wave_phase'].replace('none', 'Unclassified')

print(df.isna().sum().sort_values(ascending=False))

# Initialize dictionaries to store counts
string_none_counts = {}
nan_counts = {}

for col in df.columns:
    # Count occurrences of the string 'none' (case-insensitive) in object columns
    if df[col].dtype == 'object':
        string_none_counts[col] = df[col].astype(str).str.lower().eq('none').sum()
    else:
        string_none_counts[col] = 0 # No string 'none' in non-object columns

    # Count NaN values for all columns
    nan_counts[col] = df[col].isna().sum()

print("Count of 'none' string (case-insensitive) per column:")
display(pd.Series(string_none_counts).sort_values(ascending=False))

print("\nCount of NaN values per column:")
display(pd.Series(nan_counts).sort_values(ascending=False))

# TASK 3 — COUNTRY-WISE ANALYSIS

# 1

'''
total_cases_per_country = df.groupby('country')['cumulative_cases'].max().sort_values(ascending=False)

print("Total Cases (Top 10 Most Affected Countries):")
display(total_cases_per_country.head(10))

print("\nTotal Cases (Top 10 Safest Countries):")
display(total_cases_per_country.tail(10))
'''
# 2

'''
total_deaths_per_country = df.groupby('country')['cumulative_deaths'].max().sort_values(ascending=False)

print("\nTotal Deaths (Top 10 Most Affected Countries):")
display(total_deaths_per_country.head(10))

print("\nTotal Deaths (Top 10 Safest Countries):")
display(total_deaths_per_country.tail(10))
'''

# 3

'''
total_vaccinations_per_country = df.groupby('country')['cumulative_vaccinations'].max().sort_values(ascending=False)

print("\nTotal Vaccinations (Top 10 country)")
display(total_vaccinations_per_country.head(10))

print("\nTotal Vaccinations (Bottom 10 country)")
print(total_vaccinations_per_country.tail(10))
'''

# 4

'''
total_recoveries_per_country = df.groupby('country')['cumulative_recoveries'].max().sort_values(ascending=False)

print("\nTotal Recoveries (Top 10 country)")
display(total_recoveries_per_country.head(10))

print("\nTotal Recoveries (Bottom 10 country)")
display(total_recoveries_per_country.tail(10))

'''

# TASK 4 — GROWTH RATE ANALYSIS

# 1. Average 7-day Case Growth Rate

'''
avg_cases_growth_rate = df.groupby('country')['cases_growth_rate_7d'].mean().sort_values(ascending=False)

print("Average 7-day Case Growth Rate per Country (Top 10):")
display(avg_cases_growth_rate.head(10))

print("\nAverage 7-day Case Growth Rate per Country (Bottom 10 - potentially slowest growth or even decline):")
display(avg_cases_growth_rate.tail(10))
'''

# 2. Average 7-day Death Growth Rate
'''

avg_deaths_growth_rate = df.groupby('country')['deaths_growth_rate_7d'].mean().sort_values(ascending=False)

print("\nAverage 7-day Death Growth Rate per Country (Top 10):")
display(avg_deaths_growth_rate.head(10))

print("\nAverage 7-day Death Growth Rate per Country (Bottom 10):")
display(avg_deaths_growth_rate.tail(10))
'''

# 3. Maximum 7-day Case Growth Rate (Peak Growth)
'''

max_cases_growth_rate = df.groupby('country')['cases_growth_rate_7d'].max().sort_values(ascending=False)

print("\nMaximum 7-day Case Growth Rate per Country (Top 10 - indicating periods of rapid spread):")
display(max_cases_growth_rate.head(10))

'''

# 4. Maximum 7-day Death Growth Rate (Peak Growth)

'''
max_deaths_growth_rate = df.groupby('country')['deaths_growth_rate_7d'].max().sort_values(ascending=False)

print("\nMaximum 7-day Death Growth Rate per Country (Top 10 - indicating periods of rapid increase in deaths):")
display(max_deaths_growth_rate.head(10))

print("\nMaximum 7-day Death Growth Rate per Country (Bottom 10 - indicating periods of rapid decrease in deaths):")
display(max_deaths_growth_rate.tail(10))
'''

# TASK 5 — WAVE ANALYSIS

# 1. Which wave had the highest deaths
# Re-run after cleaning 'wave_name' from 'none' to 'Unclassified'

'''
wave_deaths = df.groupby('wave_name')['cumulative_deaths'].max().sort_values(ascending=False)
print("Wave with Highest Deaths:")
display(wave_deaths)

highest_deaths_wave = wave_deaths.idxmax()
highest_deaths_count = wave_deaths.max()
print(f"\nThe wave with the highest number of deaths is '{highest_deaths_wave}' with {highest_deaths_count:,.0f} cumulative deaths.")
'''

# 2. Which wave had the highest positivity rate

'''
wave_positivity_rate = df.groupby('wave_name')['positivity_rate_pct'].max().sort_values(ascending=False)
print("\nWave with Highest Positivity Rate (%):")
display(wave_positivity_rate)

highest_positivity_wave = wave_positivity_rate.idxmax()
highest_positivity_value = wave_positivity_rate.max()
print(f"\nThe wave with the highest positivity rate is '{highest_positivity_wave}' with {highest_positivity_value:.2f}%.")
'''

# 3. Which phase was most dangerous (based on highest positivity rate per phase)
# Interpreting 'most dangerous phase' as the phase with the highest positivity rate.
'''
phase_positivity_rate = df.groupby('wave_phase')['positivity_rate_pct'].max().sort_values(ascending=False)
print("\nWave Phase with Highest Positivity Rate (%):")
display(phase_positivity_rate)

highest_positivity_phase = phase_positivity_rate.idxmax()
highest_positivity_phase_value = phase_positivity_rate.max()
print(f"\nThe most dangerous phase (by highest positivity rate) is phase '{highest_positivity_phase}' with {highest_positivity_phase_value:.2f}%.")
'''

# TASK 6 — VACCINATION IMPACT ANALYSIS



print("Correlation between Vaccination Rate and various metrics:")

# 1.  Calculate correlation with new_cases
corr_cases = df['vaccination_rate_pct'].corr(df['new_cases'])
print(f"  - Vaccination Rate vs. New Cases: {corr_cases:.2f}")

# Calculate correlation with new_deaths
corr_deaths = df['vaccination_rate_pct'].corr(df['new_deaths'])
print(f"  - Vaccination Rate vs. New Deaths: {corr_deaths:.2f}")

# Calculate correlation with positivity_rate_pct
corr_positivity = df['vaccination_rate_pct'].corr(df['positivity_rate_pct'])
print(f"  - Vaccination Rate vs. Positivity Rate: {corr_positivity:.2f}")

print("\nNote: A negative correlation suggests that as vaccination rates increase, the other metric tends to decrease, and vice versa. Positive correlation indicates they move in the same direction.")

# TASK 7 — MOVING AVERAGE ANALYSIS

# Select a few countries for demonstration
selected_countries = ['United States', 'India', 'Brazil']

# Filter DataFrame for selected countries
df_ma = df[df['country'].isin(selected_countries)].copy()

# Ensure 'date' column is datetime type for proper sorting
df_ma['date'] = pd.to_datetime(df_ma['date'])

# Sort by country and date for correct moving average calculation
df_ma = df_ma.sort_values(by=['country', 'date'])

# Calculate moving averages for new_cases
df_ma['new_cases_ma7d'] = df_ma.groupby('country')['new_cases'].transform(lambda x: x.rolling(window=7, min_periods=1).mean())
df_ma['new_cases_ma14d'] = df_ma.groupby('country')['new_cases'].transform(lambda x: x.rolling(window=14, min_periods=1).mean())
df_ma['new_cases_ma30d'] = df_ma.groupby('country')['new_cases'].transform(lambda x: x.rolling(window=30, min_periods=1).mean())

# Calculate moving averages for new_deaths
df_ma['new_deaths_ma7d'] = df_ma.groupby('country')['new_deaths'].transform(lambda x: x.rolling(window=7, min_periods=1).mean())
df_ma['new_deaths_ma14d'] = df_ma.groupby('country')['new_deaths'].transform(lambda x: x.rolling(window=14, min_periods=1).mean())
df_ma['new_deaths_ma30d'] = df_ma.groupby('country')['new_deaths'].transform(lambda x: x.rolling(window=30, min_periods=1).mean())

print("Moving averages calculated for selected countries. Displaying a sample for 'United States':")
# Display the results for a specific country for brevity
display(df_ma[df_ma['country'] == 'United States'][['date', 'new_cases', 'new_cases_ma7d', 'new_cases_ma14d', 'new_cases_ma30d', 'new_deaths', 'new_deaths_ma7d', 'new_deaths_ma14d', 'new_deaths_ma30d']].tail())

# TASK 8 — CORRELATION ANALYSIS

# Select relevant columns for correlation analysis
correlation_columns = [
    'new_cases',
    'new_deaths',
    'rt_approx',
    'positivity_rate_pct',
    'policy_index',
    'cumulative_vaccinations'
]

# Create a subset DataFrame for correlation
df_corr = df[correlation_columns].copy()

# Drop rows with any NaN values from the selected columns for accurate correlation calculation
df_corr = df_corr.dropna()

# Calculate the correlation matrix
correlation_matrix = df_corr.corr()

print("Correlation Matrix of Key COVID-19 Metrics:")
display(correlation_matrix)

"""### TASK 9 — HIGH RISK DETECTION: Classifying Countries by Risk Level

This task aims to identify countries with high COVID-19 risk based on several key indicators:
- **Positivity Rate (`positivity_rate_pct`)**: The percentage of positive tests, indicating the spread of the virus.
- **ICU Admissions (`icu_admissions`)**: Number of patients in Intensive Care Units, reflecting severe cases.
- **Hospitalizations (`hospitalizations`)**: Total number of patients hospitalized, another measure of severity.
- **Rt Value (`rt_approx`)**: The effective reproduction number, indicating if the epidemic is growing or shrinking.

We will define thresholds for these metrics to categorize countries into 'Low Risk', 'Medium Risk', and 'High Risk' groups. For simplicity, we'll use the maximum recorded values for these metrics per country to capture the highest risk potential.
"""

# TASK 9 — HIGH RISK DETECTION: Classifying Countries by Risk Level

# Define risk thresholds (these are illustrative and can be adjusted based on expert opinion)
positivity_rate_high_threshold = 10.0 # % (e.g., above 10% is high)
positivity_rate_medium_threshold = 5.0 # % (e.g., between 5% and 10% is medium)

icu_admissions_high_threshold = 500 # e.g., above 500 ICU admissions is high
icu_admissions_medium_threshold = 100 # e.g., between 100 and 500 is medium

hospitalizations_high_threshold = 2000 # e.g., above 2000 hospitalizations is high
hospitalizations_medium_threshold = 500 # e.g., between 500 and 2000 is medium

rt_high_threshold = 1.2 # e.g., Rt above 1.2 is high risk (rapid growth)
rt_medium_threshold = 1.0 # e.g., Rt between 1.0 and 1.2 is medium risk (growth)

# Group by country and get the maximum value for each relevant metric
df_risk = df.groupby('country').agg(
    max_positivity_rate=('positivity_rate_pct', 'max'),
    max_icu_admissions=('icu_admissions', 'max'),
    max_hospitalizations=('hospitalizations', 'max'),
    max_rt_approx=('rt_approx', 'max')
).reset_index()

# Fill NaN values with 0 for metrics where max might be NaN (e.g., if a country has no data for that metric)
df_risk = df_risk.fillna(0)

# Function to assign risk level
def assign_risk(row):
    risk_score = 0

    # Positivity Rate
    if row['max_positivity_rate'] >= positivity_rate_high_threshold:
        risk_score += 3
    elif row['max_positivity_rate'] >= positivity_rate_medium_threshold:
        risk_score += 1

    # ICU Admissions
    if row['max_icu_admissions'] >= icu_admissions_high_threshold:
        risk_score += 3
    elif row['max_icu_admissions'] >= icu_admissions_medium_threshold:
        risk_score += 1

    # Hospitalizations
    if row['max_hospitalizations'] >= hospitalizations_high_threshold:
        risk_score += 3
    elif row['max_hospitalizations'] >= hospitalizations_medium_threshold:
        risk_score += 1

    # Rt Value
    if row['max_rt_approx'] >= rt_high_threshold:
        risk_score += 3
    elif row['max_rt_approx'] >= rt_medium_threshold:
        risk_score += 1

    if risk_score >= 6: # Higher score indicates higher risk
        return 'High Risk'
    elif risk_score >= 3:
        return 'Medium Risk'
    else:
        return 'Low Risk'

# Apply the risk assignment function
df_risk['risk_level'] = df_risk.apply(assign_risk, axis=1)

print("Countries classified by risk level (sample):")
#display(df_risk.sort_values(by='risk_level', ascending=False).head(10))

#display(df_risk.sort_values(by='risk_level', ascending=False).tail(10))

"""### TASK 10 — FINAL INSIGHT GENERATION

Based on our analysis through the various tasks, here are some final insights:

1.  **Which country handled COVID best?**
    *   From **Task 3 (Country-Wise Analysis)**, countries with consistently low numbers in cumulative cases and deaths, and a 'Low Risk' classification from **Task 9 (High Risk Detection)**, could be considered to have handled the pandemic effectively. For example, the `df_risk` DataFrame can be further analyzed to identify these countries.

2.  **Which wave was most dangerous?**
    *   From **Task 5 (Wave Analysis)**, we can determine the wave with the highest number of deaths and the highest positivity rate by examining the `wave_deaths` and `wave_positivity_rate` variables. This analysis highlighted which specific wave presented the most significant public health challenge in terms of fatalities and widespread infection.

3.  **Did vaccines reduce deaths?**
    *   From **Task 6 (Vaccination Impact Analysis)**, the correlation coefficients (`corr_cases`, `corr_deaths`, `corr_positivity`) indicated a very weak negative correlation between vaccination rates and new cases/deaths/positivity rates. This suggests that while vaccines might have an impact, a simple direct correlation on the full dataset might not capture the full, nuanced effect, which could be influenced by many confounding factors or time-lagged effects. Further sophisticated modeling would be required for a definitive causal conclusion.

4.  **Which factor increased spread most?**
    *   From **Task 8 (Correlation Analysis)**, we examined the `correlation_matrix`. While `rt_approx` (reproduction rate) is theoretically a direct indicator of spread, its correlation with `new_cases` was very weak. However, `positivity_rate_pct` showed a moderate positive correlation with `new_cases` and `new_deaths`. A higher `positivity_rate_pct` suggests greater community transmission or insufficient testing, both contributing to increased spread. Additionally, the `policy_index` (stringency index) showed a positive correlation with `positivity_rate_pct` (0.77), which might imply that policies were implemented in response to higher positivity rates, rather than preventing them entirely, or that the policies themselves had a mixed impact on this specific metric.
