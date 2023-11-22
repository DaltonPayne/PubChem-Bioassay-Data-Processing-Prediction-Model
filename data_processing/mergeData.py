import pandas as pd

# Load the datasets
filtered_data = pd.read_csv('output_2.csv')
numerical_features = pd.read_csv('output_3.csv')

# Merge the datasets on the 'CID' column
merged_data = pd.merge(filtered_data, numerical_features, on='CID', how='inner')

# Save the merged data to a new CSV file
merged_data.to_csv('output_4.csv', index=False)