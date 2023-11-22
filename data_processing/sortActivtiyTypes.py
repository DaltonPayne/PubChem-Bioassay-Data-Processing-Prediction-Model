import pandas as pd
import os

# Function to ensure the directory exists or create it
def ensure_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

# Read the CSV file
df = pd.read_csv('output_4.csv')

# Get unique activity types
unique_activities = df['Activity Type'].unique()

# Ensure the directory exists or create it
output_dir = 'Activity_Types'
ensure_dir(output_dir)

# Loop through unique activity types and save to separate CSV files in the new folder
for activity in unique_activities:
    # Filter the data for the current activity type
    activity_df = df[df['Activity Type'] == activity]
    
    # Create a new CSV file for the current activity type in the new folder
    output_filename = os.path.join(output_dir, f'output_{activity}.csv')
    activity_df.to_csv(output_filename, index=False)
    print(f'Data for {activity} saved to {output_filename}')
