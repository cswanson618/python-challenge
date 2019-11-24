import os
import csv

#do you need to add something to point this to a directory?

with open('election_data.csv') as e:
    vote_count = 0
    for row in e:
        rows = sum(1 for row in e)



    print("Election Results")
    print("------")
    print(rows+1)
    print
