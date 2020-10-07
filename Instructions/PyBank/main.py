import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as budgetfile:
    filereader = csv.reader(budgetfile,delimiter=",")

    #skips the header
    next(filereader)
    
    totalprofit = 0
    months = 0
    totalchange = 0
    for row in filereader:
        #calculates the total profit
        totalprofit = totalprofit + int(row[1])      
        #finds the total number of rows which will be used to determine the number of months
        months += 1
        # #to find the average change, I should create an array of each month's change, appending each iteration to the array to create it, then find the average of the array
        # ...my method below should be scrapped
        # currentprofit = 0
        # nextmonthsprofit = 0
        # currentprofit = row[1]
        # nextmonthsprofit = # i need to be able to reference the vaule in column 2 for the next row


#filler for now so the values I get are printed to the terminal
#     print("")
#     print("Financial Analysis")
#     print("-------------------")
#     print("Total Months: "+str(months))
#     print("Total Profit: $"+str(totalprofit))
#     print("totalchange????"+str(totalchange))
    

