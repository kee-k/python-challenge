#modules
import os
import csv

#set path for file
csvpath = os.path.join("Resources", "PyBank_budget_data.csv")

#set all variables to 0
months = 0
profit_loss = 0
month_change = 0
previous_month = 0
total_month_change = 0
average_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""


#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    #skip the header
    csv_header = next(csvreader)

    #loop through rows
    #row = next(csvreader)

    #every row is read 
    for row in csvreader:

        #look for months 
        #months = len(list(csvreader))
        months += 1
        ##print(months)

        #sum profits and losses
        profit_loss +=int(row[1])
        ##print(profit_loss)

        #average change
        #first calculate change from month to month
        if months > 1:
            month_change = int(row[1]) - previous_month
        #but why is it the total of monthly changes that is taken into account and not the total of profits and losses?
        total_month_change += month_change
        previous_month = int(row[1])

        average_change = round(total_month_change/months,2)
        ##print(average_change)
        
        #greatest increase
        #not entirely sure I get the logic of these two lines
        if month_change > greatest_increase:
            greatest_increase = month_change
            greatest_increase_month = row[0]
        #print(greatest_increase)
        #print(greatest_increase_month)

        #greatest decrease
        if month_change < greatest_decrease:
            greatest_decrease = month_change
            greatest_decrease_month = row[0]
        ##print(greatest_decrease)

#printing into gitbash
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

#printing to txt file
f = open("Results.txt", "w")
f.write(
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${profit_loss}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
f.close()
    
    
    
    #csvwriter = csv.writer(outputFile)

    #csvwriter.writerow(["Financial Analysis"])
    #csvwriter.writerow(["----------------------------"])
    #csvwriter([f"Total Months: {months}"])
    #csvwriter([f"Total: ${profit_loss}"])
    #csvwriter([f"Average Change: ${average_change}"])
    #csvwriter([f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})"])
    #csvwriter([f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})"])