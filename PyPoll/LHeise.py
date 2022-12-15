# Import files
import os
import csv
# Set path for file
csv_path = os.path.join('Resources', 'election_data.csv')
# Set the output of the text file
text_path = os.path.join('analysis', 'election_output.txt')
print(os.getcwd())
#Open CSV as Reader
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)
    #print(f"Header:{csv_header}")
# Set variables
    votes = 0
    total_votes_cast = 0
    candidate_s = []
    candidate_wins = {}
    winning_can = ""
    winning_count = 0
    totalvotes = 0
    popularvote = 0
    #Total votes cast
    for row in csv_reader:
        votes +=1
    # A complete list of candidates who received votes and the total number of votes won by candidate
        if row[2] not in candidate_s:
            candidate_s.append(row[2])
            candidate_wins[row[2]]=1
        else:
            candidate_wins[row[2]] = candidate_wins[row[2]] + 1

    # The total number of votes each candidate won
    # The winner of the election based on popular vote
    # Format for outputs
for i in range(len(candidate_s)):
    if winning_count < candidate_wins[candidate_s[i]]:
        winning_can = candidate_s[i]
        winning_count = candidate_wins[candidate_s[i]]
# Display Election Results Information
print("Election Results")
print("----------------------------")
print(f"Total Votes: {votes}")
print("----------------------------")

# Loop each Candidate and display their specific voting information
for i in range(len(candidate_s)):
    print(f"{candidate_s[i]}: {candidate_wins[candidate_s[i]] / votes * 100:2.3f}% ({candidate_wins[candidate_s[i]]})")

print("----------------------------")
print(f"Winner: {winning_can}")
print("----------------------------")

# Format for outputs
Output = (
    f"Election Results \n"
    f"----------------------------\n"
    f"Total Votes: {votes}\n"
    f"----------------------------\n")

for i in range(len(candidate_s)):
    Output= Output + (f"{candidate_s[i]}: {candidate_wins[candidate_s[i]] / votes * 100:2.3f}% ({candidate_wins[candidate_s[i]]})\n")

Output = Output + (
    f"----------------------------\n"
    f"Winner: {winning_can}\n"
    f"----------------------------\n")

# save results to Resources folder
with open(text_path, "w") as txtfile:
    txtfile.write(Output)
