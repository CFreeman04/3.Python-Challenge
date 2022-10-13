# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create 
# a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
import os
import csv

from csv import DictReader

# Declare variables
Votes = []
Candidates = []
CandidatesVotes = []

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as read_obj:
    csv_dict_reader=DictReader(read_obj)
    
    # Loop through CSV file
    for row in csv_dict_reader:
        Votes.append(row['Candidate'])

        # Identify all unique Candidates and initialize their vote count to 0
        if row['Candidate'] not in Candidates:
            Candidates.append(row['Candidate'])
            CandidatesVotes.append(0)

        # Add 1 vote to Candidate's Total 
        CandidatesVotes[Candidates.index(row['Candidate'])] += 1

# Display Election Results Information
print("Election Results")
print("----------------------------")
print(f"Total Votes: {len(Votes)}")
print("----------------------------")

# Loop each Candidate and display their specific voting information
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {(CandidatesVotes[i]) / len(Votes) * 100:2.3f} ({CandidatesVotes[i]})")

print("----------------------------")
print(f"Winner: {Candidates[CandidatesVotes.index(max(CandidatesVotes))]}")
print("----------------------------")

# Output files
outputFile = os.path.join("Analysis", "Election_Results.txt")

with open(outputFile,"w") as file:
    
# Write methods to print to Election_Results
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {len(Votes)}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")

    for i in range(len(Candidates)):
        file.write(f"{Candidates[i]}: {CandidatesVotes[i] / len(Votes) * 100:2.3f} ({CandidatesVotes[i]})")
        file.write("\n")

    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {Candidates[CandidatesVotes.index(max(CandidatesVotes))]}")
    file.write("\n")
    file.write("----------------------------")    