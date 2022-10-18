import csv
myfile=open("Users/elenasmcbookpro/Documents/GitHub/cloud-9-elenageller/05_Python/PY-08/Test.csv", 'r+')
print(myfile.read())
about = {
"First name": input("First name: "),
"Last name": input("Last name: "),
"Job title": input("Job title: "),
"Company": input("Company: ")
}

writer = csv.writer(myfile)
writer.writerow(about.keys())
writer.writerow(about.values())
myfile.close
myfile=open("Users/elenasmcbookpro/Documents/GitHub/cloud-9-elenageller/05_Python/PY-08/Test.csv", 'r')
print(myfile.read())