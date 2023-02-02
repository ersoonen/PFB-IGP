## This will be used as a module

#imported Path from pathlib and imported csv
from pathlib import Path
import csv

# Created fp_read variable and assigned the file path to the profit-and-loss-usd.csv to it
fp_read = Path.cwd()/"project_group4"/"csv_reports"/"profit-and-loss-usd.csv"

# Create two empty lists to store the data into the list
net_profit_list = []
net_profit_amt = []

# Using the .open() function to access the csv file which is for reading 
with fp_read.open(mode="r", encoding="UTF-8", newline="") as file:
    # Create csv reader object using csv
    reader = csv.reader(file)

    # To skip reading header 
    next(reader)
    
    # Iterate each row with 'for' loop and append the days to net_profit_list
    # and the respective net profit values to net_profit_amt
    for line in reader:
        net_profit_list.append(line)
        net_profit_amt.append(float(line[4]))

# Setup filepath to "summary_report.txt" for writing results 
fp_write = Path.cwd()/"project_group4"/"summary_report.txt"

def net_profit_diff():
    """
    - This function calculates the difference in net profit if net profit on the current
    day is lower than the previous day
    - No parameters required
    """
    
    for number in range(0,(len(net_profit_amt)-1)):
        previous_day = net_profit_amt[number]
        current_day = net_profit_amt[number+1]

        # Creates condition that if current day value is less than previous day value, it will return
        # the difference amount or the profit deficit with the latest day printed.
        if current_day < previous_day:
            difference = previous_day - current_day
            difference_day = net_profit_list[number+1][0]

            # Used if statement, summary_path and .open() method to append lines
            with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:

                # Used .write() method and f strings to create and write the days where
                # there are net profit deficit and its respective amount
                file.write(f"[NET PROFIT DEFICIT] DAY: {difference_day}, AMOUNT: USD ${difference}" + "\n")
        
        # Used elif and if the current day value is larger than the previous day, it would
        # break the loop
        elif current_day > previous_day:
            break
        
        # Used else so if there are no net profit deficit, it will write the f strings that
        # there are net profit surplus everyday
        else:
            with fp_write.open(mode="a", encoding="UTF-8", newline="") as file:
                file.write(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY" + "\n")

