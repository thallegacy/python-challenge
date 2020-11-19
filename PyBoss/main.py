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
    # Name Lists
    NameList = []
    FirstNameList = []
    LastNameList = []
    # Date Lists
    DateList = []
    Month = []
    Day = []
    Year = []
    # SSN Lists
    SSNList = []
    Last4SSN = []

    # Read and store the header row first (use next to read through data after the header)
    csv_header = next(csvreader)

    # Loop through the data after the header
    for row in csvreader:
       
       #add my elements to my lists
        EmployeeIDList.append(row[0])
        NameList.append(row[1])
        DateList.append(row[2])
        SSNList.append(row[3])

    # Loop through the Namelist to split First and Last Name
    for Name in NameList:
        FirstNameList.append(Name.split()[0])
        LastNameList.append(Name.split()[1])
 
    # Loop through the Datelist to get Day Month and Year
    for Date in DateList:
        Month.append(Date.split("-")[1])
        Day.append(Date.split("-")[2])
        Year.append(Date.split("-")[0])

    # Use List comprehension to loop and zip list to merge the date to format mm/dd/yyyy
    DateConverted = [i +"/" + j +"/"+ k for i, j, k in zip(Month, Day, Year)]
    
    for SSN in SSNList:
        Last4SSN.append(SSN.split("-")[2])

    # Use List comprehension to loop and change SSN to ***-**-NNNN format
    SSNConverted = ["***-**-" + l for l in Last4SSN]
    print(SSNConverted)
    

