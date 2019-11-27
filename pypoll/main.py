import csv
import os

print("------")
print("Please wait while votes are tabulated. This may take a minute or two.")
print("------")

path = os.path.join("pypoll", "main.py")

with open("election_data.csv") as e:
    for row in e:
        rows = sum(1 for row in e)


with open("election_data.csv") as f:
    cdte = csv.DictReader(f)
    can_list = []
    for row in cdte:
        for k, v in row.items():
                can_list.append(v)
                k= (can_list.count("Khan"))
                cor= (can_list.count("Correy"))
                ot= (can_list.count("O'Tooley"))
                li= (can_list.count("Li"))

print("Election Results")
print("------")
print("Total Votes: " + str(rows+1))
print("------")
print("Votes by candidate:")
print("")
print ("Khan recieved " + str(k) + " votes, which is " + str(round((k/(rows+1)*100),2))+ "% of the total vote")
print ("Correy recieved " + str(cor) + " votes, which is " + str(round((cor/(rows+1)*100),2))+ "% of the total vote")
print ("O'Tooley recieved " + str(ot) + " votes, which is " + str(round((ot/(rows+1)*100),2))+ "% of the total vote")
print ("Li recieved " + str(li) + " votes, which is " + str(round((li/(rows+1)*100),2))+ "% of the total vote")