#PyPoll

import os
import csv
from collections import defaultdict
from collections import Counter

#Determine which csv file version to grab
FileVersion = ['3']

#For loop
for FileToCheck in FileVersion: 
    #input file name
    csvpath = os.path.join('election_data_' + FileToCheck + '.csv' )

    #create new CVS
    PollResults = os.path.join('Poll_Results' + FileToCheck + '.csv')
#lists to store data
    Voter_ID = []
    County = []
    Candidate = []
    Total_Votes = []
    Total_by_Cand =[]
    Percent_by_Cand = []
    Winner = []

    
    with open (csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        # Skipp headers
        next(csvreader, None)
        
        for row in csvreader:
            
            #append data for candidate
            Candidate.append(row[2])

    cleanCSV = zip(Candidate)
    with open(PollResults, 'w', newline="") as csvfile:

        csvWriter = csv.writer(csvfile, delimiter=',')
        #Add headers to new CSV
        csvWriter.writerow(["Candidate"])

        #Write zipped lists to csv
        csvWriter.writerows(cleanCSV)

           


            


        




