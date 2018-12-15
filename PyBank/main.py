
import os, csv

csv_path = os.path.join("..", "PyBank", "budget_data.csv")

total_months = 0
total_revenue = 0
revenue_change_list = []
prev_month_revenue = 0
greatest_increase_month = ""
greatest_decrease_month = ""
greatest_increase_revenue = 0
greatest_decrease_revenue = 0


with open(csv_path, newline="", encoding="UTF-8") as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=",")

    for row in csv_reader:
        total_months += 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        revenue_change = int(row["Profit/Losses"]) - prev_month_revenue
        if total_months > 1:
            revenue_change_list.append(revenue_change)
        prev_month_revenue = int(row["Profit/Losses"])

        if revenue_change > greatest_increase_revenue:
            greatest_increase_revenue = revenue_change
            greatest_increase_month = row["Date"]
        if revenue_change < greatest_decrease_revenue:
            greatest_decrease_revenue = revenue_change
            greatest_decrease_month = row["Date"]

revenue_average = round(sum(revenue_change_list) / len(revenue_change_list), 2)




print("Financial Analysis for Eugene Brink, Inc") 
print("-------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${revenue_average}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_revenue})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_revenue})")

output_path = "../PyBank/Business_Data_Analysis_Eugene_Brink_Inc.txt"
with open(output_path, "w") as txt_file:
    print("Financial Analysis for Eugene Brink Inc", file = txt_file) 
    print("=======================================", file = txt_file)
    print(f"Total Months: {total_months}", file = txt_file)
    print(f"Total: ${total_revenue}", file = txt_file)
    print(f"Average Change: ${revenue_average}", file = txt_file)
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_revenue})", file = txt_file)
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_revenue})", file = txt_file)