## this will be used as module

#imported Path from pathlib and imported csv
from pathlib import Path
import csv

# created fp variable and assigned the file path to the profit-and-loss-usd.csv to it
fp = Path.cwd()/"project_group4"/"csv_reports"/"profit-and-loss-usd.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

net_profit_list = []
net_profit_amt = []

for line in reader:
    net_profit_list.append(line)
    net_profit_amt.append(float(line[4]))

summary_path = Path.cwd()/"project_group4"/"summary_reports.txt"

def net_profit_diff():
    """
    - This function calculates the difference in net profit if net profit on the current
    day is lower than the previous day
    - No parameters required.
    """
    for number in net_profit_amt:
        previous_day = net_profit_amt[number][4]
        current_day = net_profit_amt[number+1][4]

        if previous_day > current_day:
            difference = previous_day - current_day
            difference_day = net_profit_list[number+1][0]

            with summary_path.open(mode='a', encoding='UTF-8', newline="") as file:
                file.write(f"[PROFIT DEFICIT] DAY: {difference_day}", f"AMOUNT: USD{difference}" + "\n")

print(net_profit_diff())