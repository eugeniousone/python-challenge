
import os, csv

csv_path = os.path.join("..", "PyPoll", "election_data.csv")

total_votes = 0
candidate_list = []
candidate_vote = {}

with open(csv_path, newline="", encoding="UTF-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    for row in csv_reader:
        total_votes += 1
        if row["Candidate"] not in candidate_list:
            candidate_list.append(row["Candidate"])
            candidate_vote[row["Candidate"]] = 1
        else:
            candidate_vote[row["Candidate"]] += 1

sorted_candidates = [k for k in sorted(candidate_vote, key=candidate_vote.get, reverse=True)]
winner = sorted_candidates[0]

print("Election Results for Los Angeles")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------")
for candidate_name,vote_count in candidate_vote.items():
    print(candidate_name + ": " + str(round(vote_count / total_votes * 100, 4)) + "% (" + str(vote_count) + ")")
print("----------------------------------")
print(f"Winner: {winner}")
print("----------------------------------")
print("This actually worked!  Horray!!!!!")

output_path = "../PyPoll/Election_Result_for_Los_Angeles.txt"
with open(output_path, "w") as txt_file:
    print("2018 Election Results for Los Angeles", file = txt_file)
    print("-------------------------------------", file = txt_file)
    print("Total Votes: {total_votes}", file = txt_file)
    print("-------------------------------------", file = txt_file)
    for candidate_name,vote_count in candidate_vote.items():
        print(candidate_name + ": " + str(round(vote_count / total_votes * 100, 4)) + "% (" + str(vote_count) + ")", file = txt_file)
    print("-------------------------------------", file = txt_file)
    print(f"Winner: {winner}", file = txt_file)
    print("-------------------------------------", file = txt_file)
    print("This actually worked!  Horray!!!!!", file = txt_file)
