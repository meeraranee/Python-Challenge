# Import dependencies
import os
import csv

# Set file path
csvfile = os.path.join("Resources", "budget_data.csv")

# Set variables
total_months = 0
total_profit = 0
previous_profit = 0
average_change = 0
greatest_inc = 0
greatest_dec = 0
changes = []
profit = []
greatest_inc_mo = ""
greatest_dec_mo = ""
first_loop = True

# Open csv
with open(csvfile) as data:
    csvreader = csv.reader(data, delimiter = ",")
    csvheader = next(csvreader)

    # Create for loop
    for row in csvreader:
        total_months += 1
        total_profit = total_profit + (int(row[1]))

        change = (int(row[1])) - previous_profit
        changes = changes + [change]

        if first_loop == False:
            changes.append(change)

        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_mo = row[0]

        if change < greatest_dec:
            greatest_dec = change
            greatest_dec_mo = row[0]

        previous_profit = (int(row[1]))
        first_loop = False

    average_change = sum(changes)/len(changes)

# Print analysis
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {int(total_months)}")
print(f"Total: ${str(total_profit)}")
print(f"Average Change: $-{str(round(average_change, 2))}")
print(f"Greatest Increase in Profits: {greatest_inc_mo} (${greatest_inc})")
print(f"Greatest Decrease in Proftis: {greatest_dec_mo} (${greatest_dec})")

# Output text file
output_file = "output.txt"
with open(output_file,"w") as doc:
        doc.write("Financial Analysis\n")
        doc.write("----------------------------\n")
        doc.write(f"Total Months: {int(total_months)}\n")
        doc.write(f"Total: ${str(total_profit)}\n")
        doc.write(f"Average Change: $-{str(round(average_change, 2))}\n")
        doc.write(f"Greatest Increase in Profits: {greatest_inc_mo} (${greatest_inc})\n")
        doc.write(f"Greatest Decrease in Proftis: {greatest_dec_mo} (${greatest_dec})\n")