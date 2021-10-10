import os
import csv

# Path to source data
input_data = os.path.join("election_data.csv")

votes_list = []
election_list = []
candidate_list = []
unique_list = []
candidatevotes = []
votepercentage = []

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
    unique_list = list(set(candidate_list))
    cand_len = len(unique_list)


print (f" ")
print (f" ")
print (f"Election Results")
print (f"-------------------------")
print (f"Total Votes:  {total_votes}")
print (f"-------------------------")

for x in unique_list:
    candidatevotes = candidate_list.count(x)
    voterpercentage = float(candidatevotes) / float(total_votes) * 100
    print(f"{x}: {voterpercentage:.3f}% ({candidatevotes})")  
    percentage = str(voterpercentage)
    votes = str(candidatevotes)
    winningvote = max(votes)
    winner = unique_list[votes.index(winningvote)]

print (f"-------------------------")
print (f"Winner: " + str(winner) + "")
print (f"-------------------------")  
print (f" ")
print (f" ") 
    
# Path to output file
output_file = os.path.join("election_analysis.txt")

with open(output_file,'w') as text:
    text.write(" \n")
    text.write(" \n")
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Votes: " + str(total_votes) + "\n")
    text.write("-------------------------\n")
           
    for x in range(len(unique_list)):
        #text.write({unique_list[x]}percentage[x]}({votes[x]})+"\n")    
        text.write("-------------------------\n")
        text.write("Winner: (winner)\n")
        text.write("-------------------------\n")  
        text.write(" \n")
        text.write(" \n") 