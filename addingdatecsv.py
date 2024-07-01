import csv
from datetime import datetime
import pytz
import os

def add_nevada_time_to_csv(input_file, output_file):
    # Remove any extra quotes from file paths
    input_file = input_file.strip('"')
    output_file = output_file.strip('"')

    # Set the timezone to Nevada (PST)
    nevada_tz = pytz.timezone('America/Los_Angeles')

    # Read the input CSV file and write to the output CSV file
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read the header and add the new column name
        header = next(reader)
        header.append('Nevada Time (PST)')
        writer.writerow(header)

        # Process each row
        for row in reader:
            # Get current time in Nevada
            nevada_time = datetime.now(nevada_tz)
            
            # Format the time as a string
            time_str = nevada_time.strftime('%Y-%m-%d %H:%M:%S %Z')
            
            # Add the time to the row and write it
            row.append(time_str)
            writer.writerow(row)

# Example usage
input_file = r"E:\pdf2excel\Date_Time_code\cyhy-UNLV-2024-06-02T174858+0000_findings.csv"
output_file = r"E:\pdf2excel\Date_Time_code\output.csv"
add_nevada_time_to_csv(input_file, output_file)