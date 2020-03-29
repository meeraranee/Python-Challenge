import os
import csv

# Set file path
pypoll_csv_path = os.join.path("Resources", "election_data.csv")

with open(pypoll_csv_path) as csvfile:
    csv_reader = csv.read(csvfile, delimiter=',')

    for row in csv_reader:
        