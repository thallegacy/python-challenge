import os
import csv

# Path to collect data from the Resources folder
pyboss_csv = os.path.join( 'Resources', 'employee_data.csv')


# Read in the CSV file
with open(pyboss_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set your initial storage for list
    employee_id_list = []
    
    # Name Lists
    name_list = []
    first_name_list = []
    last_name_list = []
    
    # Date Lists
    date_list = []
    month = []
    day = []
    year = []
    
    # SSN Lists
    ssn_list = []
    last_4ssn = []
    
    # State Lists
    states_list = []
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
    # Read and store the header row first (use next to read through data after the header)
    csv_header = next(csvreader)

    # Loop through the data after the header
    for row in csvreader:
       
       #add each column to a separate lists
        employee_id_list.append(row[0])
        name_list.append(row[1])
        date_list.append(row[2])
        ssn_list.append(row[3])
        states_list.append(row[4])

    # Loop through the name_list to split First and Last Name
    for name in name_list:
        first_name_list.append(name.split()[0])
        last_name_list.append(name.split()[1])
 
    # Loop through the date_list to get day month and year
    for date in date_list:
        month.append(date.split("-")[1])
        day.append(date.split("-")[2])
        year.append(date.split("-")[0])

    # Use List comprehension to loop and zip list to merge the date to format mm/dd/yyyy
    date_converted = [i +"/" + j +"/"+ k for i, j, k in zip(month, day, year)]
    
    for ssn in ssn_list:
        last_4ssn.append(ssn.split("-")[2])

    # Use List comprehension to loop and change SSN to ***-**-NNNN format
    ssn_converted = ["***-**-" + l for l in last_4ssn]
   
    
    # Loop through the states list to identify the state abbreviation in the dictionary
    for state in states_list:
        state_code = us_state_abbrev[state]
        
