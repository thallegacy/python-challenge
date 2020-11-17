import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join( 'Resources', 'election_data.csv')


# Read in the CSV file
with open(pypoll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set your initial storage for list
    TotalVoterIDList = []

    # Read and store the header row first (use next to read through data after the header)
    csv_header = next(csvreader)

    # Loop through the data after the header
    for row in csvreader:
       
       #add my elements to my lists
        TotalVoterIDList.append(row[0])
  

    #print my values to Git Bash

    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: {len(TotalVoterIDList)} ')
# 