import os
import csv

months_list = []
PL_list = []

os.getcwd()
os.chdir("/Users/lorenamartinez/UTSA_BOOT_CAMP/HOMEWORK/HW3_PythonChallenge/python-challenge/PyBank/Resources")
os.getcwd()

# Path to source data
input_data = os.path.join("budget_data.csv")

# Path to output file
output_file = os.path.join("budget_analysis.txt")

# Read in CSV file
with open(input_data, 'r') as csv_file:
    budget_data = csv.reader(csv_file, delimiter=",")
    header = next(budget_data)
    
    # count months
    for row in budget_data:
        months_list.append(row)
        PL_list.append(int(row[1]))


        total_months = len(months_list)
    print (f"total months is {total_months}")

    net_total = sum(PL_list)
    print (f"net total is ${net_total}")

    # calulate net total
    #for row in range(total_months)
    #nettotal = nettotal +







    #amount_list.append(row)
    


#print(total_amount)


#    df.to_csv(filename) | Write to a CSV file


