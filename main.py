import os
import csv

#variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#file path
csvpath = os.path.join("Desktop","python-challenge", "Pypoll", "election_data.csv") 



#opening csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    print(csvreader)
       
#percentage of total votes for each candidate
percentage_khan = (khan_votes/total_votes) * 100
percentage_correy = (correy_votes/total_votes) * 100
percentage_li = (li_votes/total_votes) * 100
percentage_otooley = (otooley_votes/total_votes) * 100
    
for row in csvreader:
       
       # Total votes
        total_votes += 1

        #conditionals 
        if (row[2]) == "Khan":
            khan_votes += 1
        elif (row[2]) == "Correy":
            correy_votes += 1
        elif (row[2]) == "Li":
            li_votes += 1
        else:
            otooley_votes += 1
    
 

#Winner of election
winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

if winner == khan_votes:
    winner_name = "Khan"
elif winner == correy_votes:
    winner_name = "Correy"
elif winner == li_votes:
    winner_name = "Li"
else:
    winner_name = "O'Tooley"
    #Print results
    print(f"Election Results")
    print(f"Total Votes: {total_votes}")
    print(f"Khan: {str(percentage_khan)}")
    print(f"Correy: {str(percentage_correy)}")
    print(f"Li: {str(percentage_li)}")        
    print(f"O'Tooley: {str(percentage_otooley)}")
    print(f"Winner: {winner_name}")

