import csv
import os
#Assign variable to load file from path
file_to_load=os.path.join("Resources","election_results.csv")
# Assign variable to save the file to path
file_to_save=os.path.join("analysis","election_analysis.txt")
# Open election result and read the file
with open (file_to_load) as election_data:
    print(election_data)
    file_reader=csv.reader(election_data)
# read and print header row
    headers=next(file_reader)
    print(headers)
#open(file_to_save,"w")
# Read file object with reader function

# Print each row in election_result.csv


