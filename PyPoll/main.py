import os
import csv



os.getcwd()
os.chdir("/Users/lorenamartinez/UTSA_BOOT_CAMP/HOMEWORK/HW3_PythonChallenge/python-challenge/PyPoll/Resources")
os.getcwd()

# Path to source data
input_data = os.path.join("election_data.csv")

# Path to output file
output_file = os.path.join("election_analysis.txt")

votes_list = []
election_list = []
candidate_list = []
unique_list = []

# Read in CSV file
with open(input_data, 'r') as csv_file:
    election_data = csv.reader(csv_file, delimiter=",")
    header = next(election_data)

    for row in election_data:
     # count votes
        votes_list.append(row)
        total_votes = len(votes_list)
        election_list.append(row)

        candidate_list.append(row[2])
        







    print (f" total votes is {total_votes}  ")
    print(election_list[0])
    print(unique_list)