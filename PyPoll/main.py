#PyPoll

import os
import csv

#Determine which csv file version to grab
#FileVersion = ['1','2']


#For loop

#for FileToCheck in FileVersion:
    
    #input file name
csvpath = os.path.join('election_data_1.csv')

    #output file name
ElectionDataAnalysis = os.path.join('Election_Data_Analysis1.csv')
    
with open (csvpath, 'r') as f_in, open(ElectionDataAnalysis,'w') as f_out:
        d_reader = csv.DictReader(f_in)
        fieldnames = ['Voter ID','County','Candidate']
        d_writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        


    


