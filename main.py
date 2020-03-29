import os
import csv

file = os.join("Resources", "budget_data.csv")

with open(file) as data:
    csvreader = csv.reader(data, delimiter = ",")