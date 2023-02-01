## This will be used as a module

# Imported Path from pathlib and imported csv
from pathlib import Path
import csv

# Created fp_read variable and assigned the file path to the overheads-day-90.csv to it
fp_read = Path.cwd()/"project_group4"/"csv_reports"/"overheads-day-90.csv"

# Create 2 empty lists to store the data into the list
highest_category_list = []
highest_category_amt = []

# Using the .open() function to access the csv file which is for reading 
with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        # Create csv reader object using csv
        reader = csv.reader(file)         
        
        # To skip reading header 
        next(reader)                     
        
        # Iterate each row with 'for' loop and append the title of the overheads to highest_categrot_list
        # and the respective percentage values to highest_category_amt
        for row in reader:
            highest_category_list.append(row)
            highest_category_amt.append(float(row[1]))

# Setup filepath to "summary_report.txt" for writing results 
fp_write = Path.cwd()/"project_group4"/"summary_report.txt"

# Used def keyword to create the highest_overhead_amt() function
def highest_overhead_amt():
    """
    - This function calculates the highest overhead percentage amount
    - No parameters required
    """
    
    # Used the max() function to filter out the highest percentage value
    highest_overheads = max(highest_category_amt)

    for name in highest_category_list:
        
        # Using 'if' function to match the overhead value to the list
        if name[1] == str(highest_overheads):
            highest_overheads_title = name[0]
            
            # Used if statement, summary_path and .open() method to append lines
            with fp_write.open(mode="a", encoding="UTF8", newline="") as file: 

                # Used .write() method and f strings to create and write the highest overhead title 
                # and its respective amount       
                file.write(f"[HIGHEST OVERHEADS] {highest_overheads_title}: {highest_overheads}%" + "\n")


    


