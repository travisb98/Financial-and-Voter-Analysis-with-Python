import csv
import os

empid_list =[]
name_list=[]
dob_list=[]
ssn_list=[]
state_list=[]

master_list=[
    empid_list,
    name_list,
    dob_list,
    ssn_list,
    state_list,
]

header_list =[]
firstname_list=[]
lastname_list =[]


csvpath = os.path.join(".","employee_data.csv")

#open the CSV file
with open(csvpath,'r') as empfile:
    inputreader = csv.reader(empfile,delimiter=",")
    #defines the first row as a header list
    header_list=list(next(inputreader))

    #this works, but I'd like to be able to iterate through the each list in the master_list instead of writing out each line individually
    #could i use a comprehension to loop through the master list for this????
    for lines in inputreader:
        empid_list.append(lines[0])
        name_list.append(lines[1])
        dob_list.append(lines[2])
        ssn_list.append(lines[3])
        state_list.append(lines[4])

    
    #creates a list of last names and first names
    for fullname in name_list:
        splitname = fullname.split(" ")
        firstname_list.append(splitname[0])
        lastname_list.append(splitname[1])




print(lastname_list)


    # #doesn't work -----turns each column into a list, need to figure out how I could iterate this. maybe make a list of lists
    # for lines in inputreader:
    #     for e in master_list:
    #         for a in range(5):
    #             e.append(lines[a])
        
        # empid_list.append(lines[0])
        # name_list.append(lines[])




# print(header_list)

# print(len(header_list))

