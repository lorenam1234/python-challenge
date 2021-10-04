import os
import csv

month_list = []
amount_list = []

os.getcwd()
os.chdir("/Users/lorenamartinez/UTSA_BOOT_CAMP/HOMEWORK/HW3_PythonChallenge/python-challenge/PyBank/Resources")
os.getcwd()

# Path to source data file
input_data = os.path.join("budget_data.csv")

# Read in CSV file
with open(input_data, 'r') as csv_file:
    budget_data = csv.DictReader(csv_file)
    for row in budget_data:
        month_list.append(row)
        total_months = len(month_list)
    print (f"total months is {str(total_months)}")

    amount_list.append(row)
    total_amount = sum(budget_data)


print(total_amount)


# Calculate # months in dataset
# Use date column as dataset
#def calc_num_months(Date)


