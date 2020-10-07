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

#setting up variables
votescast = 0
khantotal = 0
correytotal = 0
litotal = 0
tooleytotal= 0
#open the CSV file
with open(csvpath) as pollfile:
    filereader = csv.reader(pollfile,delimiter=",")

    for row in filereader:
        #sums up the total number of votes cast
        votescast+=1
        if row[2]



print(votescast)