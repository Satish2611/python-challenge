# Import os module,This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#Going to csv path
csvpath=os.path.join('Resources', 'election_data.csv')
#open csv 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
# skipping Header
    csv_header=next(csvreader)
    data=[]
 #appending data- Candidate
    for row in csvreader:
        data.append(row[2])
#function for finding unique name of candidates and their occurance
    def unique(name):
        unique_name=[]
        for row in name:
            if row not in unique_name:
                unique_name.append(row)
        count=[]
#finding the unique names and count of their occurances
        for i in range(len(unique_name)):
            unique_name_count=0
            for row_1 in name:
                if unique_name[i] in row_1:
                    unique_name_count+=1
            count.append(unique_name_count)
        return unique_name,count
#calling functions and assign them to variables
unique_name,count=unique(data)
#Total votes calculation
totalvotes=len(data)
percentages=[]
#finding percentage of each candidate
for j in range(len(count)):
    percentages.append(round(count[j]/totalvotes*100,3))
    winner=percentages[0]
    winnerName=unique_name[0]
 #finding winner who has highest votes
    if winner<percentages[j]:
        winnerName=unique_name[j]
#Printing output
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")
for k in range(len(unique_name)):
    print(f"{unique_name[k]}:{percentages[k]}% ({count[k]})")
print("-------------------------")
print(f"Winner:{winnerName}")
print("-------------------------")