## This program will compute the difference in the net profit column if net profit on
# the current day is lower than the previous day.

from pathlib import Path
import csv

fp = Path.cwd()/"project_group4"/"csv_reports"/"profit-and-loss-usd.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

net_profit = []

for line in reader:
    net_profit.append(float(line[4]))

summary_path = Path.cwd()/"summary_reports.txt"

def net_profit_diff():
    """
    -
    -
    """