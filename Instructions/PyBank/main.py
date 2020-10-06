import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as budgetfile:
    filereader = csv.reader(budgetfile,delimiter=",")

    #skips the header
    next(filereader)
    #calculates the total profit
    totalprofit = 0
    for row in filereader:
        if row[0] !="":
            totalprofit = totalprofit + int(row[1])
            
        else:
            pass

def final():
    print("Financial Analysis")
    print("------------------")
    print("Total Months:"+ "input")
    print("Total Profit:" + str(totalprofit))

final()