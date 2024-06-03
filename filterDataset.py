

import csv

def contains_na(row):
    return 'NA' in row

with open('./resources/framingham.csv', 'r', newline='') as infile:
    reader = csv.reader(infile)
    headers = next(reader)  
    filtered_rows = [row for row in reader if not contains_na(row)]

with open('./resources/output.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)  
    writer.writerows(filtered_rows)  

