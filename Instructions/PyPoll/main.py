import os
import csv

#testing out using try blocks to deal with error handling regarding directory names, i should iterate this to check for each file within the project's structure.
try:
    csvpath = os.path.join("Resources","election_data.csv")
    #the filenotfound error actually came up later in the code, but I added this open(csvpath) here to check for the error early, I'm thinking this might
    #....bad bacause it's repetitive
    open(csvpath)
except FileNotFoundError:
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("encountered FileNotFoundError, assesing directory")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    csvpath = os.path.join("PyPoll","Resources","election_data.csv")

#setting up variables, dictionaries etc
votescast = 0

votedict ={"Khan":0,"Correy":0,"Li":0,"O'Tooley":0}


#open the CSV file
with open(csvpath) as pollfile:
    filereader = csv.reader(pollfile,delimiter=",")

    for row in filereader:
        #sums up the total number of votes cast
        votescast+=1
        #reads through the votedict dictionay to see if the current row matches a key in the dictionary and increases the value by 1 if it matches
        #this currently doesn't work
        for name in votedict:
            #if votedict[name] == row[2]:
            #    print("its working???")

print(votedict)




print(votescast)