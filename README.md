# DateInsertion
Utilising Date Time libraries to insert PST time in CSV's 
**Adding Date to CSV folder **

Introduction: This code adds columns to the csv files by utilizing datatime library. We must make sure what time zone we are using. 

**Libraries used: **

•	import csv -- for handling CSV files
•	from datetime -- for working with dates and times
•	import datetime -- for time zone information
•	import pytz import os -- for operating system dependent functionality

**Code Explanation: **
The function first removes any surrounding quotation marks from the file paths. It then creates a time zone object for Nevada (Pacific Time). The function opens the input file for reading and the output file for writing, ensuring consistent newline handling. It sets up CSV reader and writer objects. It reads the header row from the input file, adds a new column for Nevada time, and writes this updated header to the output file. For each subsequent row in the input file, the function gets the current time in Nevada's timezone, formats it as a string, and appends it to the row. The updated row is then written to the output file. Finally, the script sets the input and output file paths and calls the function to process the CSV file, using raw string literals to handle backslashes in file paths correctly.
