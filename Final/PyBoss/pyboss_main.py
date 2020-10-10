
import csv
import os
import datetime

us_state_dict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#-------------------------------
empid_list =[]
name_list=[]
dob_list=[]
ssn_list=[]
state_list=[]


# # below I append each of these lists under a for loop, I was hoping to make a list of these lists 
# ... to iterate through and make it less repetative, but I didn't work
# master_list=[
#     empid_list,
#     name_list,
#     dob_list,
#     ssn_list,
#     state_list,
# ]


#-------------------------------

header_list =[]
firstname_list=[]
lastname_list =[]
newdob_list =[]
newssn_list=[]
newstate_list=[]

csvpath = os.path.join("PyBoss","employee_data.csv")

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
    #formats each entry in the dob_list, formats it, then adds it tot the newdob_list
    for olddate in dob_list:
        newdob_list.append(datetime.datetime.strptime(olddate,'%Y-%m-%d').strftime('%m/%d/%Y'))
    #formats each entry in the ssn_list, formats it, then adds it to the newssn_list
    for numb in ssn_list:
        slick=slice(7,12)
        newssn_list.append("***-**"+(numb[slick]))

    #use dictionary to create new state list with full name
    for state in state_list:
        newstate = us_state_dict[state]
        newstate_list.append(newstate)
    
#adding the headers to the beining of the lists
empid_list.insert(0,header_list[0])
firstname_list.insert(0,"First Name")
lastname_list.insert(0,"Last Name")
newdob_list.insert(0,header_list[2])
newssn_list.insert(0,header_list[3])
newstate_list.insert(0,header_list[4])

# ties the multiple lists together into an object
finalrows_list=zip(
    empid_list,
    firstname_list,
    lastname_list,
    newdob_list,
    newssn_list,
    newstate_list,
)

outputpath = os.path.join("PyBoss","output_emp_data.csv")

#open the CSV file
with open(outputpath,'w+',newline='') as newempfile:
    outputwriter = csv.writer(newempfile,delimiter=",")
    for row in finalrows_list:
        outputwriter.writerow(row)
