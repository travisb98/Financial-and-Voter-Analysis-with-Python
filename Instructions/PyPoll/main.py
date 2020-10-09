import os
import csv

###error message for directory error
def errormsg():
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("encountered FileNotFoundError, assesing directory")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")

#testing out using try blocks to deal with error handling regarding directory names, i should iterate this to check for each file within the project's structure.
try:
    csvpath = os.path.join("Resources","election_data.csv")
    open(csvpath)
except FileNotFoundError:
    errormsg
    csvpath = os.path.join("PyPoll","Resources","election_data.csv")

#setting up variables, dictionaries etc
votescast = 0
votedict={}
percentagesdict={}
candidatelist =[]
uniquecandidatelist = []


#open the CSV file
with open(csvpath) as pollfile:
    filereader = csv.reader(pollfile,delimiter=",")

    next(filereader)

    for row in filereader:
        #sums up the total number of votes cast
        votescast+=1
        #adds name to candidatelist
        candidatelist.append(row[2])

    #simplifies candidate list so all entries are unique
    uniquecandidatelist = list(set(candidatelist))
    #creates a dictionary out of the candidate list to track the votes
    votedict = dict.fromkeys(uniquecandidatelist,0)


#loops through each unique vote in the candidate list and tallys the vote for each candidate's value in the dictionary
for eachvote in candidatelist:
    for name in votedict:
        if name == eachvote:
            votetally=votedict[name]
            votetally=votetally + 1
            votedict[name]=votetally
        else:
            pass
percentagesdict = dict.fromkeys(uniquecandidatelist,0.00)

#calculates each value in the percentagesdict as a percentage of total votes cast   
for candidate in percentagesdict:
    percentagesdict[candidate]="{:.3%}".format(votedict[candidate]/votescast)

# # i need this code explained to me, it returs a tuple instead of the voter's name
# winner = max([(value,key) for key, value in votedict.items()])
# winner = winner[1]

winner = max(votedict,key=lambda key:votedict[key])


print (percentagesdict)
print ("Winner: "+ str(winner))

#print (votedict)
# print(candidatelist)
# print(votescast)
# print(votedict)

  
    # ###this just loops through the dictionary and adds 1 to the value if the name is khan
    # for name in votedict:
    #     derpy = 'Khan'
    #     if name == derpy:
    #         votetally=votedict[name]
    #         votetally=votetally + 1
    #         votedict[name]=votetally

    # ####testing this one prints out each value in the  dictionary
    # for name in votedict:
    #     print(votedict[name])
    
    # #testing  prints out->   dict_keys(['Candidate', 'Khan', 'Correy', 'Li', "O'Tooley"])
    # print(votedict.keys()) 

    # ####testing this one prints out each value in the dictionary
    # for name in votedict.values():
    #     print(name)

    # ### testing this one prints out each key in the dictionary individually
    # for name in votedict:
    #     print (name)

    # ###testing prints out each value individaually
    # for votetally in votedict:
    #     print(votedict[votetally])

    # ###this just loops through the dictionary and adds 1 to the value if the name is khan
    # derpy = "Khan"
    # for name in votedict:
    #     if name == derpy:
    #         votetally=votedict[name]
    #         votetally=votetally + 1
    #         votedict[name]=votetally
