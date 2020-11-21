import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join( 'Resources', 'election_data.csv')


# Read in the CSV file
with open(pypoll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set your initial storage for list
    total_voterid_list = []
    total_candidate_list = []

    # Read and store the header row first (use next to read through data after the header)
    csv_header = next(csvreader)

    # Loop through the data after the header
    for row in csvreader:
       
       #add my elements to my lists
        total_voterid_list.append(row[0])
        total_candidate_list.append(row[2])

    #Get the count of each candidate and store it in variables
    khan = total_candidate_list.count("Khan")
    correy = total_candidate_list.count("Correy")
    li = total_candidate_list.count("Li")
    otooley= total_candidate_list.count("O'Tooley")
    
    #Get the vote percentages of each candidate and store it in variables
    total_count = khan + correy + li + otooley
    khanpct = (khan / total_count) * 100
    correypct = (correy / total_count) * 100
    lipct = (li / total_count) * 100
    otooleypct= (otooley / total_count) * 100
    
    # Find the winning candidate
    if khan > correy and khan > li and khan > otooley:
        winner = "Khan"
    elif correy > khan and correy > li and correy > otooley:
        winner = "Correy"
    elif li > khan and li > correy and li > otooley:
        winner = "Li"
    else:
        winner = "O'Tooley"    
    
    #print my values to Git Bash

    print("Election Results")
    print("----------------------------")
    print(f'Total Votes: {len(total_voterid_list)} ')
    print("----------------------------")
    print(f'Khan: {round(khanpct,2)}% ({khan}) ')
    print(f'Correy: {round(correypct,2)}% ({correy}) ')
    print(f'Li: {round(lipct,2)}% ({li}) ')
    print(f"O'Tooley: {round(otooleypct,2)}% ({otooley}) ")
    print("----------------------------")
    print(f'Winner: {winner} ')
    print("----------------------------")

# Specify the file to write to
output_path = os.path.join( "analysis", "election_results.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as textfile:
    
    # input the results in the text file
    textfile.write("Election Results")
    textfile.write("\n----------------------------")
    textfile.write(f'\nTotal Votes: {len(total_voterid_list)} ')
    textfile.write("\n----------------------------")
    textfile.write(f'\nKhan: {round(khanpct,2)}% ({khan}) ')
    textfile.write(f'\nCorrey: {round(correypct,2)}% ({correy}) ')
    textfile.write(f'\nLi: {round(lipct,2)}% ({li}) ')
    textfile.write(f"\nO'Tooley: {round(otooleypct,2)}% ({otooley}) ")
    textfile.write("\n----------------------------")
    textfile.write(f'\nWinner: {winner} ')
    textfile.write("\n----------------------------")
