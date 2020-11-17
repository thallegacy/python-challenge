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
    TotalCandidateList = []

    # Read and store the header row first (use next to read through data after the header)
    csv_header = next(csvreader)

    # Loop through the data after the header
    for row in csvreader:
       
       #add my elements to my lists
        TotalVoterIDList.append(row[0])
        TotalCandidateList.append(row[2])

    #Get the count of each candidate and store it in variables
    Khan = TotalCandidateList.count("Khan")
    Correy = TotalCandidateList.count("Correy")
    Li = TotalCandidateList.count("Li")
    OTooley= TotalCandidateList.count("O'Tooley")
    
    #Get the vote percentages of each candidate and store it in variables
    TotalCount = Khan + Correy + Li + OTooley
    Khanpct = (Khan / TotalCount) * 100
    Correypct = (Correy / TotalCount) * 100
    Lipct = (Li / TotalCount) * 100
    OTooleypct= (OTooley / TotalCount) * 100
    
    # Find the winning candidate
    if Khan > Correy and Khan > Li and Khan > OTooley:
        Winner = "Khan"
    elif Correy > Khan and Correy > Li and Correy > OTooley:
        Winner = "Correy"
    elif Li > Khan and Li > Correy and Li > OTooley:
        Winner = "Li"
    else:
        Winner = "O'Tooley"    
    
    #print my values to Git Bash

    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: ({len(TotalVoterIDList)}) ')
    print("----------------------------")
    print(f'Khan: {round(Khanpct,2)}% ({Khan}) ')
    print(f'Correy: {round(Correypct,2)}% ({Correy}) ')
    print(f'Li: {round(Lipct,2)}% ({Li}) ')
    print(f"O'Tooley: {round(OTooleypct,2)}% ({OTooley}) ")
    print("----------------------------")
    print(f'Winner: {Winner} ')
    print("----------------------------")
