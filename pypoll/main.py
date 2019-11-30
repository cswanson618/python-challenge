import csv
import os
from statistics import mode #Found from a StackOverflow search on finding the mode of a list. Also affects line 52.
import sys #Using to execute a method to print terminal output to text (see lines 72-83). Found using research on StackOverflow.

print("------")
print("Please wait while votes are tabulated. This may take a moment or two.")
print("------")

path = os.path.join("..","pypoll", "election_data.csv")

with open(path) as e:
    for row in e:
        rows = sum(1 for row in e)

#Lines 12-14 merely calculate the number of total votes there are by summing the number 
#of rows in the CSV file in a for loop

print ("There were " + str(rows) + " total votes cast.")
print("------")

with open(path) as f:
    cdte = csv.DictReader(f)
    first_list = []
    can_list = []
    for row in cdte:
        for k, v in row.items():
                first_list.append(v)

#It seemed most logical to me to now reopen the CSV as a dictionary so that I could parse keys and values
#and place values in a list. I do this by creating a new list by where the for loop appends dictionary
#values to a new list. I found line 26 in Python Dictionaries documentation. I also discovered (after much toil) that dictionaries
#imported by the DictReader method produce a new dictionary for every row, hence the loop in a loop. The first
#loop loops the rows, the second loops the keys and values in each row.

can_list = first_list [2::3]
unique_candidateset = set(can_list)
unique_candidateslist = list(unique_candidateset)

#Line 36 is responsible for getting rid of the Voter ID and County Data by focusing on the index point
#in the first_list where the candidate data is, then returning every third item (note: each row was Voter ID,
# County ID, Candidate. Thus, we start at the Candidate index point and keep going to every third index point
# in the list). This creates a list of just the candidate names from the original CSV. 
# I then use the set function in python to get a list of the unique Candidate values, and convert that 
# set back to a list. Thus can_list is a list of just the candidate names from the CSV while
#unique_candidateslist is a list that has just the unique names of the candidates who recieved votes

index_count = 0
for index_count in range (0, (len(unique_candidateslist))):
    print(str(unique_candidateslist[index_count])+ ": " \
    + str((can_list.count(unique_candidateslist[index_count]))) + \
    " votes, which is " + str((round(((can_list.count(unique_candidateslist[index_count])/rows)*100), 2))) \
    + "% of the total vote.")
    index_count += 1
print("------")
print(str(mode(can_list)) + " is the winner of the election.") #See comment at line 3.


#Finally, my code creates a for loop by where the loop uses the list count function to check the unique names
#in the unique_candidateslist against how many times they appear in the list that shows how many times
#each candidate's name appears (can_list). The loop iterates through the index points in the unique candidates
#list to do this. Using the range function and making the end of the range the list length of the 
#unique candidates list keeps me from going out of bounds. The rest of the code is just the mathematical 
#operations to get percentages of the total vote for each candidate. The winner tabulation is derived from 
#the mode of can_list.
# 
# This code is entirely independent of any specific candidate name or total number of votes;
#everything is calculated inside the code. That is why the division to get the percentages refers to the 
#calculation of the total number of votes cast as coded in lines 12-14 and the list.count method uses the lists
#derived from the dictionaries created from the original CSV.

savepath= os.path.join("..", "pypoll", "election_tabulation.txt")
f= open (savepath, "w+")
sys.stdout =f
print("Election Results")
print("------")
print ("There were " + str(rows) + " total votes cast.")
print("------")
index_count = 0
for index_count in range (0, (len(unique_candidateslist))):
    print(str(unique_candidateslist[index_count])+ ": " \
    + str((can_list.count(unique_candidateslist[index_count]))) + \
    " votes, which is " + str((round(((can_list.count(unique_candidateslist[index_count])/rows)*100), 2))) \
    + "% of the total vote.")
    index_count += 1
print("------")
print(str(mode(can_list)) + " is the winner of the election.")
f.close()
#The above lines repeat the code that outputs the election results to the terminal so it will now print to a text file.
#As described at line 4, I found this method using a search on Stack Overflow.