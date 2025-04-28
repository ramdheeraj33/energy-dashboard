
import pandas as pd

# Load data
df = pd.read_csv('../data/raw/seattle_building_energy_sample.csv')

# Feature Engineering
df['EUI'] = df['energy_consumption_kwh'] / df['building_area_sqft']
df['Cost_per_Sqft'] = df['energy_cost_usd'] / df['building_area_sqft']
df['is_anomaly'] = (df['energy_consumption_kwh'] > df['energy_consumption_kwh'].rolling(window=2).mean() * 1.5)

# Save cleaned data
df.to_csv('../data/processed/cleaned_energy_data.csv', index=False)
print("✅ ETL pipeline completed.")
