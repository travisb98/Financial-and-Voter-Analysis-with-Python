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
    csvpath = os.path.join("PyBank","Resources","budget_data.csv")

#open the CSV file
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

#defines the final results as a function so they can be printed to the terminal and the text document
def final(x):
    x("")
    x("Financial Analysis")
    x("-------------------")
    x("Total Months: "+str(months))
    x("Total Profit: $"+str(totalprofit))
    x("Average Change:$"+str(averagechange))
    x("Greatest Increase: "+winnermonth+"($"+str(gincrease)+")")
    x("Greatest Decrease: "+losermonth+"($"+str(gdecrease)+")")

#prints the results to the terminal
final(print)

#opening the results textfile and the results. !!!!formatting within the text document is currently garbage!!!!!
try:
    resultspath = os.path.join("analysis","PYBANK_results.txt")
    #
    #
    open(resultspath)
except FileNotFoundError:
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("encountered FileNotFoundError, assesing directory")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    resultspath = os.path.join("PyBank","analysis","PYBANK_results.txt")

with open(resultspath,'w') as resultsfile:
    final(resultsfile.write)
