# Add dependencies
import csv
import os
#Assign variable to load file from path
file_to_load=os.path.join("Resources","election_results.csv")
# Assign variable to save the file to path
file_to_save=os.path.join("analysis","election_analysis.txt")
#Initilize total vote counter.
total_votes=0

# declare list for candidate options and dictionary for candidate.
candidate_options=[]
candidate_votes={}
#Create a county list and county votes dictionary.
county_options=[]
county_votes={}

#track winning candidate,vote_count and vote percentage
winning_candidate=""
winning_count=0
winning_percentage=0 
#Track the largest county and county voter turnout.
largest_county=""
largest_county_count=0
largest_county_percentage=0 

# Open election result and read the file
with open (file_to_load) as election_data:
    print(election_data)
    file_reader=csv.reader(election_data)
# read and print header row
    headers=next(file_reader)
    print(headers)
# for each row in CSV file
    for row in file_reader:
    #Add to the total vote_count
        total_votes+=1
        
    # get the candidate name from each row
        candidate_name=row[2]
    #Extract county name in each row
        county_name=row[1]
        # If candidate does not mathch with exsting candidate
        #add to the candidate list
        if candidate_name not in candidate_options:
            #Add candidate name in candidate list
            candidate_options.append(candidate_name)
            #Start the candidate votes counter
            candidate_votes[candidate_name]=0
            #Add candidate votes.
        candidate_votes[candidate_name]+=1
    # If county does not mathch with exsting county
        #add to the county list
        if county_name not in county_options:
            #Add the existing county to the list of counties.
            county_options.append(county_name)
            #Start the county votes counter
            county_votes[county_name]=0
            #Add county votes.
        county_votes[county_name]+=1
# Save election result to text file.
with open(file_to_save,"w") as election_analysis:
#After opening the file print the final vote count to the terminal.#
    election_results=(
        f"\n election_results\n"
        f"-------------------------\n"
        f"Total Votes={total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results,end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    election_analysis.write(election_results)
        #print(candidate_votes)       
    election_analysis.write("county votes:\n")
    #get the county from the county dictionary.
    for county_name in county_votes:
            #Retrieve the county vote count.
            votescounty= county_votes[county_name]
            #Calculate the percentage of votes for the county.
            county_vote_percentage=float(votescounty)/float(total_votes)*100
            #Print the county results to the terminal.
            countywise_vote_count=(f"{county_name}: {county_vote_percentage:.1f}% ({votescounty:,})\n")
            # Print each county's voter count and percentage to the terminal.
            print(countywise_vote_count)
            # Save the county votes to a text file.
            election_analysis.write(countywise_vote_count)
            #Write an if statement to determine the winning county and get its vote count.
            if (votescounty>largest_county_count)and (county_vote_percentage>largest_county_percentage):
                largest_county_count=votescounty
                largest_county_percentage=county_vote_percentage
                largest_county=county_name
    largest_county_summary=(
            f"--------------------------\n"
            f"Largest county turnout:{largest_county}\n"
            f"-------------------------\n")
    #Print the county with the largest turnout to the terminal.
    print(largest_county_summary)
    #Save the county with the largest turnout to a text file.
    election_analysis.write(largest_county_summary)

    for candidate_name in candidate_votes:
        #Retrive vote count and percentage
            votes= candidate_votes[candidate_name]
            vote_percentage=float(votes)/float(total_votes)*100
            candidate_result=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            # Print each candidate's voter count and percentage to the terminal.
            print(election_results)
            #  Write each candidate's voter count and percentage to the text file.
            election_analysis.write(candidate_result)
            # Determine winning vote count, winning percentage, and candidate.
            if (votes>winning_count)and (vote_percentage>winning_percentage):
                winning_count=votes
                winning_percentage=vote_percentage
                winning_candidate=candidate_name
    # Print the winning candidate (to terminal)
    winning_candidate_summary=(
            f"--------------------------\n"
            f"winning candidate:{winning_candidate}\n"
            f"winning vote count:{winning_count:,}\n"
            f"winning vote percentage:{winning_percentage:.1f}"
            f"\n-------------------------\n")
    #Save candidate result to text file.
    election_analysis.write(winning_candidate_summary)
     
    