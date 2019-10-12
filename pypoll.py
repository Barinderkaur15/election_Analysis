
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Creating a filename variable to save file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter 
total_votes=0 
# Candidate Options
candidate_options = []
candidate_votes={}
# open the election data 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    # to do :read and analyze data here 
    file_reader=csv.reader(election_data)

    headers=next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # add to total vote count 
        total_votes+=1
         # Print the candidate name from each row.
        candidate_name = row[2]
         # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
         # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
           # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1

 # Save the results to our text file.
with open(file_to_save, "w") as txt_file:    # be careful with Intend other wise give IO error
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    # Determine the Percentage of votes for each candidate
    # 1.Iterate through the candidate list 
    for candidate in candidate_votes: 
    #2. Retrieve vote count of a candidate 
        votes=candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results= (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        #f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
