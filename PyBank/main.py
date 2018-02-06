#PyBank

import os
import csv
from collections import defaultdict
import numpy as np

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

    Month_count = 0
    Total_Rev = 0
    ListValues = []
    Max_Inc = 0


    for record in d_reader:
        record['Date'] = str(record['Date'])
        Month_count+=1
        record['Revenue'] = int(record['Revenue'])
        d_writer.writerow(record)
        Total_Rev+=record['Revenue']
        ListValues.append(int(record['Revenue']))
    x = np.array(ListValues)
    Monthly_Change = np.diff(x)
    Avg_Change = sum(Monthly_Change)/Month_count
    Max_Inc = max(Monthly_Change)
    Min_Inc = min(Monthly_Change)
    

    print("\n")
    print("Financial Analysis", "\n")
    print("-------------------","\n")
    print("Total Months: ", Month_count)
    print("Total Revenue: $", Total_Rev)
    print("Average Revenue Change: $", Avg_Change)
    print("Greatest Increase in Revenue: $", Max_Inc)
    print("Greatest Decrease in Revenue: $", Min_Inc)
    print("\n")










