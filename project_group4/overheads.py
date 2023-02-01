## will be used as a module

## import required modules
from pathlib import Path
import csv

## setup file path for reading
fp_read = Path.cwd()/"project_group4"/"csv_reports"/"overheads-day-90.csv"

highest_category_list = []
highest_category_amt = []

with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        reader = csv.reader(file) # create csv reader object using csv        
        
        # to skip reading header 
        next(reader)                     
        
        # iterate each row with loop
        for row in reader:
            highest_category_list.append(row)
            highest_category_amt.append(float(row[1]))

## setup filepath for writing results 
fp_write = Path.cwd()/"project_group4"/"summary_reports.txt"

def highest_function():
    
    highest_overheads = max(highest_category_amt)

    for name in highest_category_list:
        
        if name[1] == str(highest_overheads):
            highest_overheads_title = name[0]
            
            # write the result to a text file
            with fp_write.open(mode="w", encoding="UTF8", newline="") as file:        
                file.write(f"[HIGHEST OVERHEADS] {highest_overheads_title}: {highest_overheads}%" + "\n")


    


