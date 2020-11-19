import os
import csv

# Path to collect data from the Resources folder
pyboss_csv = os.path.join( 'Resources', 'employee_data.csv')


# Read in the CSV file
with open(pyboss_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set your initial storage for list
    EmployeeIDList = []
    NameList = []
    FirstNameList = []
    LastNameList = []


    # Read and store the header row first (use next to read through data after the header)
    csv_header = next(csvreader)

    # Loop through the data after the header
    for row in csvreader:
       
       #add my elements to my lists
        EmployeeIDList.append(row[0])
        NameList.append(row[1])

    # Loop through the Namelist to split First and Last Name
    for i in NameList:
        FirstNameList.append(i.split()[0])
        LastNameList.append(i.split()[1])
 
    

