## PyPoll

#### Overview

In PyPoll we had to create a Python script that analyzes the votes and calculates each of the following:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote.

#### My Method:

- Create a path to collect data from the Resources folder
- Read in the CSV file and split the data on the commas
- Identify the columns I want to reference from the CSV and set up empty lists to prepare to store those columns in the lists  (totalvoteridlist, totalcandidatelist)
- Loop through the data after the header. While looping
  - Add my column elements to the empty lists I created (totalvoteridlist, totalcandidatelist)
- Get the count of each candidate and store it in variables using their names as identifiers
- Get the total votes by adding the counts of each candidate together
- Determined the winner by comparing the counts of each candidate using a conditional
  - The candidate with the greatest value compared to the others was the winner
- Print the results of my calculations to the command terminal
  - Total Votes-number of elements in the totalvoteridlist list
  - Each candidates percentages and counts as calculated previously
  -  Winner as determined previously
- Specify the text file to write to
- Open the file using "write" mode. Specify the variable to hold the contents
- Input the results in the text file