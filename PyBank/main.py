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
    NetChangeList = []
    previous = 0

    # Read and store the header row first (use next to read through data after the header)
    csv_header = next(csvreader)

    # Loop through the data after the header
    for row in csvreader:
       
       #add my elements to my lists
        TotalMonthsList.append(row[0])
        TotalAmountList.append(int(row[1]))
        
        #Get the percent change and then add my elements to my lists
        netchange=int(row[1]) - previous
        NetChangeList.append(netchange)
        previous =int(row[1])
    
    total= sum(TotalAmountList)
    NetChangeList.pop(0)
    averagechange  =sum(NetChangeList)/ len(NetChangeList)
    
    #print my values
    print(f'Total Months: {len(TotalMonthsList)} ')
    print(f'Total Amount: ${total} ')
    print(f'Average Change: {round(averagechange,2)} ')