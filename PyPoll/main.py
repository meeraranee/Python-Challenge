# Import dependencies
import os
import csv

# Set variables
total_votes = 0
candidates = []
candidate_votes = {}
vote_count = 0
vote_percent = []
winning_candidate = ""
winning_count = 0

# Set file path
pypoll_csv_path = os.path.join("Resources", "election_data.csv")

# Open csv
with open(pypoll_csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)

    for row in csv_reader:
        total_votes +=1
        candidate = row[2]
        
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate]=0
        candidate_votes[candidate]+=1

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes)/float(total_votes)*100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percent:.3f}% ({votes})"
        


# Print analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"{candidate}: {int(vote_percent)}% {vote_count}")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

# Output text file
output_file = "output.txt"
with open(output_file,"w") as doc:
        doc.write("Election Results\n")
        doc.write("-------------------------\n")
        doc.write(f"Total Votes: {total_votes}\n")
        doc.write(f"-------------------------\n")
        doc.write(f"{candidate}: {int(vote_percent)}% {vote_count}\n")
        doc.write(f"-------------------------\n")
        doc.write(f"Winner: {winning_candidate}\n")
        doc.write("-------------------------")