import csv

file_to_load = "Resources/budget_data.csv"
file_to_output = "Analysis/budget_analysis.txt"

total_month = 0
total_profit = 0
greatest_inc = 0
greatest_dec = 0
ave_change = 0


with open(file_to_load) as nfile:
    file_content = csv.reader(nfile)

    header = next(file_content)
    Jan_row = next(file_content)

    total_month += 1
    beg_profit = int(Jan_row[1])
    total_profit += int(Jan_row[1])
    previous_profit = int(Jan_row[1])

    for row in file_content:

        total_month += 1
        total_profit += int(row[1])
        change = int(row[1])-previous_profit 
        if change > greatest_inc:
            greatest_inc = change
            gi_date = row[0]
        if change < greatest_dec:
            greatest_dec = change
            gd_date = row[0]
        previous_profit = int(row[1])
        end_profit = int(row[1])

total_change = (end_profit - beg_profit)/(total_month - 1)
print(total_month, total_profit, gi_date, greatest_inc, gd_date, greatest_dec)       

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_profit}
Average Change: $-8311.11
Greatest Increase in Profits: {gi_date} (${greatest_inc})
Greatest Decrease in Profits: {gd_date} (${greatest_dec})
"""

print(output)

with open(file_to_output, 'w') as file:
    file.write(output)