import csv
myFile = open("py8.csv", "r+")
print(myFile.read())


req_info = ["First Name", "Last Name", "Job Titel", "Company"] 
myDict = {
    "First Name": " ",
    "Last Name": " ",
    "Job Titel": " ",
    "Company" : " ",

    }

myDict ["First Name"] = input("WHat is your First Name? ")
myDict ["Last Name"] = input("What is your Last Name? ")
myDict ["Job Titel"] = input("What is your job titel? ")
myDict ["Company"] = input("What is your current company where you work?")

print (myDict) 
writer = csv.writer(myFile)
writer.writerow(myDict.values())
myFile.close()
myFile = open("py8.csv", "r")
print(myFile.read())