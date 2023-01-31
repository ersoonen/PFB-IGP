## this will be used as module
from pathlib import Path
import csv

## This will be called "COH_diff module"
fp = Path.cwd()/"project_group4"/"csv_reports"/"cash-on-hand-usd.csv"

# Create 2  empty lists to store the data into the list
cash_on_hand_list = []
cash_on_hand_amt = []

# Using the .open() function to access the csv file which is for reading
with fp.open(mode ="r", encoding = "UTF-8", newline = "") as file:
    # .reader reads the data in the csv file
    readfiles = csv.reader(file)
    next(readfiles)

    # Create a loop
    for line in readfiles:
        cash_on_hand_list.append(line)
        cash_on_hand_amt.append(float(line[1]))

summary_path = Path.cwd()/"summary_reports.txt"

def cash_on_hand_diff():
    for number in range(0,(len(cash_on_hand_amt)-1)):
        first_day = cash_on_hand_amt[number]
        second_day = cash_on_hand_amt[number+1]

        if first_day > second_day:
            difference = first_day - second_day
            difference_day = cash_on_hand_list[number+1][0]

            with summary_path.open(mode='a', encoding='UTF-8') as file:
                file.write(f"[CASH DEFICIT] DAY{difference_day}, AMOUNT : USD{difference}" + "\n")


