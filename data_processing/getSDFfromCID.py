import pandas as pd
import requests
import os
import math
from tqdm import tqdm  # Import the tqdm function

def get_sdf(cid):
    url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{int(cid)}/record/SDF'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f'Failed to fetch SDF for CID {int(cid)}: {response.status_code} - {response.reason}')

def main():
    # Load the data from the CSV file
    data = pd.read_csv('output_2.csv')

    # Extract the CIDs from the data
    cids = data['cid'].tolist()

    # Ensure the sdf directory exists
    os.makedirs('sdf', exist_ok=True)

    # Fetching SDF for each CID with a progress bar
    for cid in tqdm(cids, desc="Fetching SDF", unit="compound"):
        # Skip if cid is NaN
        if math.isnan(cid):
            print(f'Skipping invalid CID: {cid}')
            continue

        # Check if the SDF file already exists, if so skip fetching
        filepath = os.path.join('sdf', f'CID_{int(cid)}.sdf')
        if os.path.exists(filepath):
            print(f'SDF file for CID {int(cid)} already exists, skipping.')
            continue

        sdf = get_sdf(cid)
        if sdf:
            print(f'Successfully fetched SDF for CID {int(cid)}')
            # Save the SDF data to a file in the sdf directory
            with open(filepath, 'w') as file:
                file.write(sdf)

if __name__ == "__main__":
    main()
