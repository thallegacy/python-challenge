import os
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join( 'Resources', 'budget_data.csv')


# Read in the CSV file
with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set your initial storage for list
    total_months_list = []
    total_amount_list = []
    net_change_list = []
    previous = 0

    # Read and store the header row first (use next to read through data after the header)
    csv_header = next(csvreader)

    # Loop through the data after the header
    for row in csvreader:
       
       #add my elements to my lists
        total_months_list.append(row[0])
        total_amount_list.append(int(row[1]))
        
        #Get the percent change and then add my elements to my lists
        net_change= int(row[1]) - previous
        net_change_list.append(net_change)
        previous = int(row[1])
    
    # Get the Total Amount
    total= sum(total_amount_list)
    # Get the Average Changet
    net_change_list.pop(0)
    average_change  = sum(net_change_list)/ len(net_change_list)
    # Get indices to use for Increase and Decrease in Profits
    maxindex = net_change_list.index(max(net_change_list))
    minindex = net_change_list.index(min(net_change_list))

    #print my values to Git Bash

    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {len(total_months_list)} ')
    print(f'Total Amount: ${total} ')
    print(f'Average Change: {round(average_change,2)} ')
    print(f'Greatest Increase in Profits: {total_months_list[maxindex+1]} (${max(net_change_list)}) ')
    print(f'Greatest Decrease in Profits: {total_months_list[minindex+1]} (${min(net_change_list)}) ')

    # Specify the file to write to
output_path = os.path.join( "analysis", "financial_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as textfile:
    
    # input the results in the text file
    textfile.write('Financial Analysis ')
    textfile.write('\n----------------------------')
    textfile.write(f'\nTotal Months: {len(total_months_list)} ')
    textfile.write(f'\nTotal Amount: ${total} ')
    textfile.write(f'\nAverage Change: {round(average_change,2)} ')
    textfile.write(f'\nGreatest Increase in Profits: {total_months_list[maxindex+1]} (${max(net_change_list)}) ')
    textfile.write(f'\nGreatest Decrease in Profits: {total_months_list[minindex+1]} (${min(net_change_list)}) ')