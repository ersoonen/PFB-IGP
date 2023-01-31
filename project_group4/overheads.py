## will be used as a module

## import required modules
from pathlib import Path
import csv

## inspect what is cwd
print(Path.cwd())

## setup file path for reading
fp_read = Path.cwd()/"project_group4"/"csv_reports"/"dbs_data_1.csv"

## to confirm fp setup
print(fp_read.exists()) 

## setup filepath for writing results 
fp_write = Path.cwd()/"project_group4"/"dbs_avg_cp.txt"

## create the file
fp_write.touch()
print(fp_write.exists()) 

########

def dbsacp_function():    
    fp_read = Path.cwd()/"project_group4"/"csv_reports"/"dbs_data_1.csv"    
    fp_write = Path.cwd()/"project_group4"/"dbs_avg_cp.txt"    
    fp_write.touch()
   
    cp_list= []
 
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:        
        reader = csv.reader(file) # create csv reader object using csv        
        next(reader)              
        # to skip reading header        
        for row in reader:        # iterate each row with loop            
            print(row)            # just to inspect, can remove later            
            cp_list.append(float(row[2]))
 
        # print(cp_list)  # just to check, can remove later
 
        # Calculate average closing price        
        avg_cp = sum(cp_list)/len(cp_list)
 
    # write the result to a text file    
    with fp_write.open(mode="w", encoding="UTF8", newline="") as file:        
        file.write(f"average closing price for DBS = SGD{avg_cp}")

