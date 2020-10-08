import os
import csv
#error message for directory error
def errormsg():
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")
    print("encountered FileNotFoundError, assesing directory")
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")

#testing out using try blocks to deal with error handling regarding directory names, i should iterate this to check for each file within the project's structure.
try:
    csvpath = os.path.join("Resources","budget_data.csv")
    open(csvpath)
except FileNotFoundError:
    try:
        errormsg
        csvpath = os.path.join("PyBank","Resources","budget_data.csv")
        open(csvpath)
    except FileNotFoundError:
        errormsg
        csvpath = os.path.join("Instructions","PyBank","Resources","budget_data.csv")


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
    #calculates the average change   
    averagechange = round(totalchange/(months-1),2)
# defining the final results as a function so it can be printed to the terminal and the text document
def final(x):
    breaky = "\n"
    x(f'{breaky}Financial Analysis{breaky}-------------------{breaky}Total Months: ${months}{breaky}Total Profit: ${totalprofit}{breaky}Average Change: ${averagechange}{breaky}Greatest Increase {winnermonth} (${gincrease}){breaky}Greatest Decrease: {losermonth} (${gdecrease})')

#prints the results to the terminal
final(print)

#checks the directory and prints the results to the PYBANK_results.txt file
try:
    resultspath = os.path.join("analysis","PYBANK_results.txt")
    open(resultspath,'w+')
except FileNotFoundError:
    try:
        errormsg
        resultspath = os.path.join("PyBank","analysis","PYBANK_results.txt")
        open(resultspath,'w+')
    except FileNotFoundError:
        errormsg
        resultspath = os.path.join("Instructions","PyBank","analysis","PYBANK_results.txt")
        open(resultspath,'w+')

with open(resultspath,'w+') as resultsfile:
    final(resultsfile.write)
