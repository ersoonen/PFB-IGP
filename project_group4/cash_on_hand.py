## This will be used as a module

# Imported Path from pathlib and imported csv
from pathlib import Path
import csv

# Created fp_read variable and assigned the file path to the cash-on-hand-usd.csv to it
fp_read = Path.cwd()/"project_group4"/"csv_reports"/"cash-on-hand-usd.csv"

# Create 2 empty lists to store the data into the list
cash_on_hand_list = []
cash_on_hand_amt = []

# Using the .open() function to access the csv file which is for reading
with fp_read.open(mode ="r", encoding = "UTF-8", newline = "") as file:
    # .reader reads the data in the csv file
    reader = csv.reader(file)

    # To skip reading header
    next(reader)

    # Create a for loop and used it to loop through and append the days to cash_on_hand_list
    # and their respective cash on hand values to cash_on_hand_amt
    for line in reader:
        cash_on_hand_list.append(line)
        cash_on_hand_amt.append(float(line[1]))

# Setup filepath to "summary_report.txt" for writing results 
fp_write = Path.cwd()/"project_group4"/"summary_report.txt"

# Used def keyword to create the COH_diff() function
def COH_diff():
    """
    - This function calculates the difference in cash on hand if cash on hand on the
    current day is lower than the previous day
    - No parameters required
    """
    
    # Used len(cash_on_hand_amt)-1 because we had 7 days (44-50) we just want 6 days (45-50)
    for number in range(0,(len(cash_on_hand_amt)-1)):
        previous_day = cash_on_hand_amt[number]
        current_day = cash_on_hand_amt[number+1]

        # Creates condition that if current day value is less than previous day value, 
        # it will return the difference amount or the cash deficit with the latest day printed.
        if current_day < previous_day:
            difference = previous_day - current_day
            difference_day = cash_on_hand_list[number+1][0]


            # Used if statement, summary_path and .open() method to append lines
            with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
                
                # Used .write() method and f strings to create and write the days where
                # there are cash deficit and its respective amount
                file.write(f"[CASH DEFICIT] DAY: {difference_day}, AMOUNT: USD{difference}" + "\n")

    



