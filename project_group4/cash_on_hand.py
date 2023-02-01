## this will be used as module

# imported Path from pathlib and imported csv
from pathlib import Path
import csv

## This will be called "COH_diff module"
fp_read = Path.cwd()/"project_group4"/"csv_reports"/"cash-on-hand-usd.csv"

# Create 2 empty lists to store the data into the list
cash_on_hand_list = []
cash_on_hand_amt = []

# Using the .open() function to access the csv file which is for reading
with fp_read.open(mode ="r", encoding = "UTF-8", newline = "") as file:
    # .reader reads the data in the csv file
    readfiles = csv.reader(file)
    next(readfiles)

    # Create a for loop and used it to loop through and append the days to cash_on_hand_list
    # and their respective cash on hand values to cash_on_hand_amt
    for line in readfiles:
        cash_on_hand_list.append(line)
        cash_on_hand_amt.append(float(line[1]))

# created fp_write variable and assigned the path to the summary_report.txt to it
fp_write = Path.cwd()/"project_group4"/"summary_report.txt"

# Used def keyword to create the cash_on_hand_diff() function
def cash_on_hand_diff():
    """
    - This function calculates the difference in cash on hand if cash on hand on the
    current day is lower than the previous day
    - No parameters required.
    """
    
    # 
    for number in range(0,(len(cash_on_hand_amt)-1)):
        first_day = cash_on_hand_amt[number]
        second_day = cash_on_hand_amt[number+1]

        # 
        if first_day < second_day:
            difference = second_day - first_day
            difference_day = cash_on_hand_list[number+1][0]


            # Used if statement, summary_path and .open() method to append lines
            with fp_write.open(mode='a', encoding='UTF-8', newline="") as file:
                
                # used .write() method and f strings to create and write the days where
                # there are cash deficit and its respective amount
                file.write(f"[CASH DIFFERENCE] DAY: {difference_day}, AMOUNT: USD ${difference}" + "\n")
                



