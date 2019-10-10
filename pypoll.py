
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Creating a filename variable to save file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# open the election data
with open(file_to_load) as election_data:

    # to do :read and analyze data here 
    file_reader=csv.reader(election_data)
    # to print each row in the csv
    #for row in file_reader:
        #print(row)
    #Read and print header row.
    headers=next(file_reader)
    print(headers)