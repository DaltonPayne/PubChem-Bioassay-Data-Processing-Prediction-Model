import csv

# Define the names of the input and output files
input_file = 'output_1.csv'
output_file = 'output_2.csv'

# Read in the data from the input file
with open(input_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    headers = next(reader)  # Store the headers
    data = list(reader)  # Convert the reader object to a list to store the data

# Sort the data based on the Activity Type (assuming it's the second column)
sorted_data = sorted(data, key=lambda row: row[1])

# Write the sorted data to the output file
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Write the headers
    writer.writerow(headers)
    # Write the sorted data
    writer.writerows(sorted_data)
