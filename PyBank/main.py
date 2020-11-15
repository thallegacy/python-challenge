import os
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join( 'Resources', 'budget_data.csv')


# Read in the CSV file
with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set your initial storage for list
    TotalMonthsList = []
    TotalAmountList = []
  
    # Read and store the header row first (use next to read through data after the header)
    csv_header = next(csvreader)

    # Loop through the data after the header
    for row in csvreader:
       
       #add my elements to my lists
        TotalMonthsList.append(row[0])


    #print my values
    print(f'Total Months: {len(TotalMonthsList)} ')
 