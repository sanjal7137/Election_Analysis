import csv
import os
#Assign variable to load file from path
file_to_load=os.path.join("Resources","election_results.csv")
# Assign variable to save the file to path
file_to_save=os.path.join("analysis","election_analysis.txt")
total_votes=0
candidate_options=[]
candidate_votes={}
winning_candidate=""
winning_count=0
winning_percentage=0 
# Open election result and read the file
with open (file_to_load) as election_data:
    print(election_data)
    file_reader=csv.reader(election_data)
# read and print header row
    headers=next(file_reader)
    print(headers)
    for row in file_reader:
        total_votes+=1
        candidate_name=row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1
with open(file_to_save,"w") as election_analysis:
    election_results=(
        f"\n election_results\n"
        f"-------------------------\n"
        f"Total Votes={total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results,end="")
    election_analysis.write(election_results)
        #print(candidate_votes)       
     
    for candidate_name in candidate_votes:
            votes= candidate_votes[candidate_name]
            vote_percentage=float(votes)/float(total_votes)*100
            candidate_result=(f"{candidate_name}:recived  {vote_percentage:.1f}% ({votes:,})\n")
            election_analysis.write(candidate_result)
            if (votes>winning_count)and (vote_percentage>winning_percentage):
                winning_count=votes
                winning_percentage=vote_percentage
                winning_candidate=candidate_name
    winning_candidate_summary=(
            f"--------------------------\n"
            f"winning candidate:{winning_candidate}\n"
            f"winning vote count:{winning_count}\n"
            f"winning vote percentage:{winning_percentage:.1f}")
    election_analysis.write(winning_candidate_summary)
    
        
        

        
        
        
    
    
        


#open(file_to_save,"w")
# Read file object with reader function

# Print each row in election_result.csv


