import csv

#do you need to add something to point this to a directory?

with open("election_data.csv") as e:
    for row in e:
        rows = sum(1 for row in e)

        print("Election Results")
        print("------")
        print("Total Votes: " + str(rows+1))

with open("election_data.csv") as f:
    list_dict = csv.DictReader(f)
    for row in list_dict:
        
        print("------")
        print (Khan)