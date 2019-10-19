
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Creating a filename variable to save file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter 
total_votes_candidate=0 
total_votes_county=0
# Candidate Options
candidate_options = []
candidate_votes={}   
 # County Options
County_options=[]
county_votes={}
# open the election data and read the data 
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_county_count=0
Winning_county=""
winning_county_percentage = 0
with open(file_to_load) as election_data:
   
    file_reader=csv.reader(election_data)

    headers=next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Adding total vote count  
        total_votes_county+=1   
        county_name = row[1]
         
        if county_name not in County_options:
         # Add the county name to the list if not present using append
            County_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name]+=1
  
        #For Candidate : add the name of the candidate 
        total_votes_candidate+=1
        candidate_name = row[2]
         
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]+=1

 
with open(file_to_save, "w") as txt_file:  
    # Total number of votes   
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes_county:,}\n"
        f"-------------------------\n")
     
    print(election_results, end="")
    txt_file.write(election_results)

    for county in county_votes: 
        # Results for each county 
        votes=county_votes[county]
        vote_percentage = float(votes) / float(total_votes_county) * 100
        county_results= (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        
        print(county_results)
        txt_file.write(county_results)  # Will right result to the text file 
         # Reports the largest county rurnout 
        if(votes>winning_county_count) and (vote_percentage>winning_county_percentage):
            winning_county_count=votes
            winning_county_percentage=vote_percentage
            winning_county=county

    winning_county_summary = (
       
        f"-------------------------\n"
        f"Largest County Turnover: {winning_county}\n"
      #  f"Winning Vote Count: {winning_count:,}\n"
      #  f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_county_summary,end="")
    txt_file.write(winning_county_summary)

    for candidate in candidate_votes: 
    # Retrieve vote count of a candidate 
        votes=candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes_candidate) * 100
        candidate_results= (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)  # to writethe results in text file
