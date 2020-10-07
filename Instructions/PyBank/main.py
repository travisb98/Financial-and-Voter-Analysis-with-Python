import os
import csv

#testing out using try blocks to deal with error handling regarding directory names, i should iterate this to check for each file within the project's structure.
try:
    csvpath = os.path.join("Resources","budget_data.csv")
    #the filenotfound error actually came up later in the code, but I added this open(csvpath) here to check for the error early, I'm thinking this might
    #....bad bacause it's repetitive
    open(csvpath)
except FileNotFoundError:
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("encountered FileNotFoundError, assesing directory")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    csvpath = os.path.join("PYBANK","Resources","budget_data.csv")

#open 
with open(csvpath) as budgetfile:
    filereader = csv.reader(budgetfile,delimiter=",")

    #skips the header
    next(filereader)
    
    # setting arrays and variables
    totalprofit = 0
    months = 0
    currentprofit = 0
    prevmonthprofit = 0
    currentchange = 0
    totalchange = 0
    gincrease = 0
    gdecrease = 0

    #reads the file
    for row in filereader:
        #calculates the total profit, commented out because I'm using the array to do this
        totalprofit = totalprofit + int(row[1])      
        #finds the total number of rows which will be used to determine the number of months
        months += 1
        
        #skips the first row and calculates the changes and greatest increase/decrease
        if months > 1:
            currentprofit = int(row[1])
            currentchange= currentprofit - prevmonthprofit
            totalchange += currentchange
            if currentchange > gincrease:
                gincrease = currentchange
                winnermonth =row[0]
            if currentchange < gdecrease:
                gdecrease = currentchange
                losermonth=row[0]

        
        #during the first iteration of the for loop, the if block is skipped and the previous month's profit is set to the first row's value
        prevmonthprofit = int(row[1])
        
    averagechange = round(totalchange/(months-1),2)


def final();
    print("")
    print("Financial Analysis")
    print("-------------------")
    print("Total Months: "+str(months))
    print("Total Profit: $"+str(totalprofit))
    print("Average Change:$"+str(averagechange))
    print("Greatest Increase: "+winnermonth+"($"+str(gincrease)+")")
    print("Greatest Decrease: "+losermonth+"($"+str(gdecrease)+")")

final():








#opening the results textfile and writing filler text
try:
    resultspath = os.path.join("analysis","PYBANK_results.txt")
    #
    #
    open(resultspath)
    close(resultspath)
except FileNotFoundError:
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("encountered FileNotFoundError, assesing directory")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    resultspath = os.path.join("PYBANK","analysis","PYBANK_results.txt")

with open(resultspath,'w') as resultsfile:
    resultsfile.write("this is test text")
