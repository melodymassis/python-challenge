#PyBank

import os
import csv
from collections import defaultdict
from collections import Counter


#Determine which csv file version to grab
#FileVersion = ['1']

#Loop through files

#input file name
csvfile = os.path.join('..', 'PyBank', 'budget_data_1.csv' )

#output file name
NewCSV = os.path.join('..', 'PyBank', 'Analysis.csv' )

with open(csvfile, 'r') as RawData, open(NewCSV, 'w') as f_out:
    csvReader = csv.reader(RawData, delimiter=',')
    d_reader = csv.DictReader(RawData)
    fieldnames=['Date','Revenue']
    d_writer = csv.DictWriter(f_out, fieldnames=fieldnames)

    for record in d_reader:
        record['Date'] = str(record['Date'])
        record['Revenue'] = int(record['Revenue'])
        d_writer.writerow(record)
        print(record)











