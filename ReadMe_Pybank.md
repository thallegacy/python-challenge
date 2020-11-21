## Pybank

#### Overview

In Pybank we had to create a Python script that analyzes the records to calculate each of the following:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in losses (date and amount) over the entire period

#### My Method:

- Create a path to collect data from the Resources folder
- Read in the CSV file and split the data on the commas
- Identify the columns I want to reference from the CSV and set up empty lists to prepare to store those columns in the lists  (totalmonthslist, totalamountlist)
- Set up an empty list and variable to use to calculate the changes in Profit/Losses
- Read and store the header row first (use next to read through data after the header)
- Loop through the data after the header. While looping
  - Add my column elements to the empty lists I created (totalmonthslist, totalamountlist)
    - totalamountlist list elements were turn into integers for calculation purposes
  - Calculate the changes in Profit/Losses
    - Capture the Profit/Losses as in integer and subtract the current row from the previous row
    - Take the results and add it to the empty list (netchangelist)
    - Repeat the process until the all the calculated elements are in the netchangelist list
- Calculated the net total amount of "Profit/Losses" using the sum function on the elements of the totalamountlist list
- Removed the first element of the netchangelist list
  - This value was calculate with an initial value of zero as there was would not have been a previous value in the first row
- Calculated the average of the Profit/Losses 
  - Sum of the netchangelist list elements over the number of elements in the list (length)
- For the greatest increase in profits and greatest decrease in losses I use the min and max value of the netchangelist
  - Stored the index locations of the locations to use to identify the locate the months associated with the values
- Print the results of my calculations to the command terminal
  - Total Months -number of elements in the totalmonthslist list
  - Total Amount- the value of total that was calculated
  -  Average Change - the value of average that was calculated
  - Greatest Increase in Profit - the value of max calculated
    - To find the month associated , I use the max index  from netchangelist + 1 as a value was remove from the netchangelist list
  - Greatest Decrease in Profits - the value of max calculated
    - To find the month associated , I use the min index  from netchangelist + 1 as a value was remove from the netchangelist list
- Specify the text file to write to
- Open the file using "write" mode. Specify the variable to hold the contents
- Input the results in the text file