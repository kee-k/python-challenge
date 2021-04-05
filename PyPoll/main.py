#modules
import os
import csv

#set path for file
csvpath = os.path.join("Resources", "PyPoll_election_data.csv")

#set all variables to 0
total_votes = 0
percentage_votes = 0
total_candidate_votes = 0
winner = ""
winning_count = 0

#create an empty list
candidates = []

#create an empty dictionary
candidate_dict = {}

#empty list for percentage votes
percentage_votes_list = []

#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    #skip the header
    csv_header = next(csvreader)

    #every row is read 
    for row in csvreader:

        #total number of votes overall 
        total_votes += 1

        #candidate list
        
        candidate_name = row[2]

        #getting votes per candidate
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_dict[candidate_name] = 1 
        else:
            candidate_dict[candidate_name] += 1

    #getting dictionary values i.e. candidate vote numbers    
    dict_values = list(candidate_dict.values())
    # print(dict_values)

    #getting dictionary keys i.e. candidate names
    dict_keys = list(candidate_dict.keys())
    # print(dict_keys)

    #looping through to get percentages
    for x in dict_values:
        # total_candidate_votes = candidate_dict.get()
        percentage_votes = float(x/total_votes * 100)
        # print(percentage_votes)
        percentage_votes_list.append(percentage_votes)
        
    #looping through to find winner
    for candidate in candidate_dict:
        candidate_value = (candidate_dict[candidate])
        # print(candidate_value)
        if (candidate_value > winning_count):
            winning_count = candidate_value
            winner = candidate
            # print(winner)
        
    # for x in candidate_dict:
    #     candidate_dict[candidate_name]/total_votes * 100
    #     print (x)


# print(percentage_votes_list)

# print(total_votes)
# print(candidates)
# print(candidate_dict)

# print(total_candidate_votes)
# print(percentage_votes)

# print(candidate_dict/total_votes * 100)


# printing into gitbash
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"{dict_keys[0]}:{percentage_votes_list[0]:.3f}% ({dict_values[0]})")
print(f"{dict_keys[1]}:{percentage_votes_list[1]:.3f}% ({dict_values[1]})")
print(f"{dict_keys[2]}:{percentage_votes_list[2]:.3f}% ({dict_values[2]})")
print(f"{dict_keys[3]}:{percentage_votes_list[3]:.3f}% ({dict_values[3]})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")


#printing to txt file
f = open("Results.txt", "w")
f.write(
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
    f"{dict_keys[0]}:{percentage_votes_list[0]:.3f}% ({dict_values[0]})\n"
    f"{dict_keys[1]}:{percentage_votes_list[1]:.3f}% ({dict_values[1]})\n"
    f"{dict_keys[2]}:{percentage_votes_list[2]:.3f}% ({dict_values[2]})\n"
    f"{dict_keys[3]}:{percentage_votes_list[3]:.3f}% ({dict_values[3]})\n"
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n")
f.close()

