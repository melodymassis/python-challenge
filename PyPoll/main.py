#PyPoll

import os
import csv
from collections import defaultdict
from collections import Counter

#Determine which csv file version to grab
FileVersion = ['1','2']

#For loop
for FileToCheck in FileVersion: 
    #input file name
    csvpath = os.path.join('election_data_' + FileToCheck + '.csv' )

#lists to store data
    Voter_ID = []
    County = []
    Candidate = []
    Total_Votes = []
    Total_by_Cand =[]
    Percent_by_Cand = []
    Winner = []

    
    with open (csvpath, 'r') as csvpath:
        csvreader = csv.reader(csvpath, delimiter=",")
        # Skipp headers
        next(csvreader, None)
        
        for row in csvreader:
            
            #append data for candidate
            Candidate.append(row[2])
            Total_Votes = defaultdict(Candidate)

            Total_by_Cand = {}
            for w in range(len(Candidate)):
                if w in Total_by_Cand:
                    Total_by_Cand[w]+=1
                else:
                    Total_by_Cand[w]=1
            print (Total_by_Cand) 
            


            


        




