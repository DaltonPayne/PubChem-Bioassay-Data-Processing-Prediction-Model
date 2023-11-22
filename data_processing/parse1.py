import csv

# Define the input file names
input_files = ['pubchem_protacxn_P14416_bioactivity_protein.csv']
output_file = 'output_1.csv'

def process_row(row):
    """Extracts relevant data from a row."""
    cid = row[4]  # Assuming the 5th column is CID
    acname = row[12]  # Assuming the 13th column is Activity Type
    acqualifier = row[13]  # Assuming the 14th column is Qualifier
    acvalue = row[14]  # Assuming the 15th column is Value
    
    # If any value is 'NULL', return None
    if 'NULL' in (cid, acname, acqualifier, acvalue):
        return None
    
    return [cid, acname, acqualifier, acvalue]

# Container for the extracted data
activity_data = []

# Read and process each input file
for input_file in input_files:
    with open(input_file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)  # Skip the headers
        for row in reader:
            processed_row = process_row(row)
            if processed_row is not None:  # Only append if the row is not None
                activity_data.append(processed_row)

# Write the extracted data to the output file
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Write the headers
    writer.writerow(['cid', 'acname', 'acqualifier', 'acvalue'])
    # Write the data
    writer.writerows(activity_data)
