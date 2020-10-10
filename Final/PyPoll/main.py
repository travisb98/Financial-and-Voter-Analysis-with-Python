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


winner = max(votedict,key=lambda key:votedict[key])

#printing the final results to terminal, prints in random order since I'm referencing dictionaries
print("Election Results")
print("-----------------------")
print("Total Votes: "+ str(votescast))
print("-----------------------")
for candidate in uniquecandidatelist:
    print(candidate+": " + str(percentagesdict[candidate])+" ("+str(votedict[candidate])+")")
print("-----------------------")
print ("Winner: "+ str(winner))
print("-----------------------")

try:
    resultspath = os.path.join("analysis","PYPOLL_results.txt")
    open(resultspath,'w+')
except FileNotFoundError:
        errormsg
        resultspath = os.path.join("PyPoll","analysis","PYPOLL_results.txt")
        open(resultspath,'w+')

with open(resultspath,'w+') as resultsfile:
    write=resultsfile.write
    write("Election Results\n")
    write("-----------------------\n")
    write("Total Votes: "+ str(votescast)+"\n")
    write("-----------------------\n")
    for candidate in uniquecandidatelist:
        write(candidate+": " + str(percentagesdict[candidate])+" ("+str(votedict[candidate])+")\n")
    write("-----------------------\n")
    write ("Winner: "+ str(winner)+"\n")
    write("-----------------------\n")
