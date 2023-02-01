## will be used as a module

## import required modules
from pathlib import Path
import csv

## setup file path for reading
fp_read = Path.cwd()/"project_group4"/"csv_reports"/"overheads-day-90.csv"

## setup filepath for writing results 
fp_write = Path.cwd()/"project_group4"/"summary_reports.txt"

def highest_function():    
    fp_read = Path.cwd()/"project_group4"/"csv_reports"/"overheads-day-90.csv"    
    fp_write = Path.cwd()/"project_group4"/"summary_reports.txt"    
    fp_write.touch()
   
    highest_category_list= []
 
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        reader = csv.reader(file) # create csv reader object using csv        
        
        # to skip reading header 
        next(reader)                     
        
        # iterate each row with loop
        for row in reader:
            highest_category_list.append(float(row[1]))
 
        # created category vairable and used max() to find the highest value in
        # highest_category_list. Assigned this value to the category variable
        category = max(highest_category_list)
 
    # write the result to a text file
    with fp_write.open(mode="w", encoding="UTF8", newline="") as file:        
        file.write(f"[HIGHEST OVERHEADS] {}: {category}%" + "\n")

