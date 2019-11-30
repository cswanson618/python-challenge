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
    first_list = []
    can_list = []
    for row in cdte:
        for k, v in row.items():
                first_list.append(v)

can_list = first_list [2::3]
unique_candidateset = set(can_list)
unique_candidateslist = list(unique_candidateset)

index_count = 0
for index_count in range (0, (len(unique_candidateslist))):
    print(can_list.count(unique_candidateslist[index_count]))
    index_count += 1

    
print ("All candidates who recieved votes: " + str(unique_candidateslist))
print("------")         

# print("Election Results")
# print("------")
# print("Total Votes: " + str(rows))
# print("------")
# print("Votes by candidate:")
# print("")
# print ("Khan recieved " + str(k) + " votes, which is " + str(round((k/(rows+1)*100),2))+ "% of the total vote")
# print ("Correy recieved " + str(cor) + " votes, which is " + str(round((cor/(rows+1)*100),2))+ "% of the total vote")
# print ("O'Tooley recieved " + str(ot) + " votes, which is " + str(round((ot/(rows+1)*100),2))+ "% of the total vote")
# print ("Li recieved " + str(li) + " votes, which is " + str(round((li/(rows+1)*100),2))+ "% of the total vote")
# print("------")
# print("Winner is:")
# if (k == cor):
#     print ("Tie between Khan and Correy")
# elif (k == ot):
#     print ("Tie between Khan and O'Tooley")
# elif (k == li):
#     print ("Tie between Khan and Li")
# elif (cor == ot):
#     print ("Tie between Correy and O'Tooley")
# elif (cor == li):
#     print ("Tie between Correy and Li")
# elif (ot == li):
#     print ("Tie between O'Tooley and Li")
# elif (k > cor) and (k > ot) and (k > li):
#     print("Khan")
# elif (cor > k) and (cor > ot) and (cor > li):
#     print("Correy")
# elif (ot > k) and (ot > cor) and (ot > li):
#     print("O'Tooley")
# elif (li > k) and (li > cor) and (li > ot):
#     print("Li")
# else:
#     print("ERROR. Please notify Christopher Swanson.")
# print ("------")
# print ("End of tabulation")