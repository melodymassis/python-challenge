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
    Total = []

    
    with open (csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        # Skipp headers
        next(csvreader, None)
        
        Total_Votes = 0
        
        for row in csvreader:
            if row[2] not in Candidate:
            #append data for candidate
                Candidate.append(row[2])
                print(Candidate)
            else:
                Total_Votes+=1
                print(Total_Votes)  
                             
            #add count by candidate
            Total_by_Cand = 0
            for i in range(len(Candidate)):
                if Candidate == Candidate:
                    Total_by_Cand+=1
                    print(Total_by_Cand)
                                
                else:
                    Total_by_Cand+=0
            Total = str(Total_Votes)

    # Zip and write results in new CSV file
    cleanCSV = zip(Candidate, Total)
    with open(PollResults, 'w', newline="") as csvfile:

        csvWriter = csv.writer(csvfile, delimiter=',')
        #Add headers to new CSV
        csvWriter.writerow(["Candidate","Total_by_Cand"])

        #Write zipped lists to csv
        csvWriter.writerows(cleanCSV)