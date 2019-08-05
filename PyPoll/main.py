import os
import csv

poll_data = os.path.join(os.path.dirname(__file__), '..', 'Resources', 'election_data.csv')

with open(poll_data, newline="") as poll:
    csv_header = next(poll)   
    csv_reader = list(csv.reader(poll, delimiter=","))
  
    print(f"Header:{csv_header}")
    # for row in csv_reader:
    #     print(row)
#   *The total number of votes cast
total_votes = len(csv_reader)

#   *A complete list of candidates who received votes
#defining a function does not execute until we call the function and pass data into it to operate on 
#poll_data = full data set
def unique(poll_data):
    unique_candidates = []
    for x in poll_data:
        if x[2] not in unique_candidates:
            unique_candidates.append(x[2])
    return unique_candidates 

#called the function and passed csv_reader into function to be operated on
#what you pass it will be the actual data
#store return value in variable 
candidates = unique(csv_reader)

#  *The total number of votes each candidate won
#candidate name will be the key: candidate value will be number of votes they have
def candidate_votes(candidates,poll_data):
    unique_votes = {}
    for name in candidates:

        #adding the first candidates name in the dictionary, and they have 0 votes to start
        unique_votes[name] = 0
        for row in poll_data: 

            #for the row that we are looking at, if it is the same as the current candidate name, we will add a vote for them
            if row[2] == name:
                unique_votes[name] += 1
    return unique_votes
vote_count = candidate_votes(candidates,csv_reader)

file = open("Poll_Analysis.txt","w") 
print(f"Total Votes: {total_votes}")
file.write(f"Total Votes: {total_votes}")

#   *The percentage of votes each candidate won
for name, votes in vote_count.items():
    percentage = (votes/total_votes)*100
    print(f"{name}: {round(percentage,3)}% ({votes})")
    file.write(f"{name}: {round(percentage,3)}% ({votes})")
#get max value by pulling out the values in the dictionary, gives us a list of the dictionary
vote_max = max(vote_count.values())

#using value to retreive the dictionary key-key and value have same index
Winner = list(vote_count.keys())[list(vote_count.values()).index(vote_max)]
print(f"Winner: {Winner}")
file.write(f"Winner: {Winner}")
file.close()
