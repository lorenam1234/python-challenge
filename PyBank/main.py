import os
import csv

months_list = []
PL_list = []
change_list = []


os.getcwd()
os.chdir("/Users/lorenamartinez/UTSA_BOOT_CAMP/HOMEWORK/HW3_PythonChallenge/python-challenge/PyBank/Resources")
os.getcwd()

# Path to source data
input_data = os.path.join("budget_data.csv")

# Read in CSV file
with open(input_data, 'r') as csv_file:
    budget_data = csv.reader(csv_file, delimiter=",")
    header = next(budget_data)
    
  
    for row in budget_data:
       # count months
       months_list.append(row)
       total_months = len(months_list)
       
       # calculate net total
       PL_list.append(int(row[1]))
       net_total = sum(PL_list)
 
    # Calc average changes in Profit/Losses 
    item = 0
    prev_item = 0
    for item in range (1,total_months):
        if item == 0:
            change_list.append(0)
        else:
            change_list.append(int(PL_list[item])-int(PL_list[prev_item]))
            prev_item += 1
        total_change = sum(change_list)
        avg_change = total_change/len(change_list)

    increased_profit = max(change_list)
    decreased_profit = min(change_list)
    increased_idx = change_list.index(increased_profit)+1
    decreased_idx = change_list.index(decreased_profit)+1
    increased_month = (months_list[increased_idx])
    decreased_month = (months_list[decreased_idx])

    # Display output
    #output
    print (f" ")
    print (f" ")
    print (f"Financial Analysis")
    print (f"-------------------------")
    print (f"Total Months: {total_months}")  
    print (f"Total: $" + str(net_total))
    print (f"Average Change: ${round((avg_change),2)}")
    print (f"Greatest Increase in Profits: {increased_month[0]} $ {increased_profit}")
    print (f"Greatest Decrease in Profits: {decreased_month[0]} $ {decreased_profit}")
    print (f" ")
    print (f" ")

# Path to output file
os.getcwd()
os.chdir("/Users/lorenamartinez/UTSA_BOOT_CAMP/HOMEWORK/HW3_PythonChallenge/python-challenge/PyBank/analysis")
os.getcwd()

output_file = os.path.join("budget_data_analysis.txt")

with open(output_file,'w') as text:
    text.write(" \n")
    text.write(" \n")
    text.write("Financial Analysis\n")
    text.write("-------------------------\n")
    text.write("Total Months: " + str(total_months) +"\n")  
    text.write("Total: $" + str(net_total) + "\n")
    text.write("Average Change: $ " + str(avg_change) +"\n")
    text.write("Greatest Increase in Profits: " + str(increased_month) + " $" + str(increased_profit)+ "\n")
    text.write("Greatest Decrease in Profits: " + str(decreased_month) + " $" + str(decreased_profit)+ "\n")
    text.write(" ")
    text.write(" ")
