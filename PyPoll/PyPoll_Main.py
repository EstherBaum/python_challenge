import csv

tot_votes = 0
greatest_votes = 0
candidates = []
votes_one = 1
votes_two = 1
votes_three = 1

file_to_output = "Analysis/election_data.txt"
csvpath = "Resources/election_data.csv"

with open(csvpath) as csvreader:
    csvfile = csv.reader(csvreader)

    header = next(csvfile)

#find all the different candidates

    for row in csvfile:
        tot_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
        elif row[2] == candidates[0]:
            votes_one += 1
            if votes_one > greatest_votes:
                greatest_votes = votes_one
                winner = candidates[0]
        elif row[2] == candidates[1]:
            votes_two += 1
            if votes_two > greatest_votes:
                greatest_votes = votes_two
                winner = candidates[1]
        elif row[2] == candidates[2]:
            votes_three += 1
            if votes_three > greatest_votes:
                greatest_votes = votes_three
                winner = candidates[2]

one_perc = round(votes_one/tot_votes*100, 3)
two_perc = round(votes_two/tot_votes*100, 3)
three_perc = round(votes_three/tot_votes*100, 3)


print(tot_votes, one_perc, votes_one, two_perc, votes_two, three_perc, votes_three, winner)

output = f"""
Election Results
-------------------------
Total Votes: {tot_votes}
-------------------------
Charles Casper Stockham: {one_perc}% ({votes_one})
Diana DeGette: {two_perc}% ({votes_two})
Raymon Anthony Doane: {three_perc}% ({votes_three})
-------------------------
Winner: {winner}
-------------------------
"""
print(output)

with open(file_to_output, 'w') as file:
    file.write(output)

    

