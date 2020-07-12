import csv

from pip._vendor.distlib.compat import raw_input
from tabulate import tabulate
import pandas as pd
import fileinput
import re
welcome = 'welcome to insight academy'.title()
print(welcome)
with open('student_list.csv','a',newline='') as file:
    writer=csv.writer(file,delimiter='|')
    # writer.writerow(['Name','Address','Contact','Enrolled_course','Payment','Due'])


print("For course List Enter          1: ")
print("For student Registration Enter 2: ")
print("For student list Enter         3: ")
print("For updating students Enter    4: ")
print("For deleting students Enter    5: ")

num =int(input("Enter the value: "))

if num==1:
    with open('course_list.csv', 'r') as c:
        data = pd.read_csv(c)
        print(tabulate(data, headers='keys', tablefmt='psql'))

if num ==2:
    name=str(input("Enter the name: "))
    Address=str(input("Enter the Address: "))
    Contact=int(input("Enter the contact number: "))
    enrolled_course=str(input("Enter the enrolled course: "))
    payment=str(input("Enter the payment: "))
    due=str(input("Enter the due amount: "))
    with open('student_list.csv', 'a+', newline='') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow([name,Address, Contact, enrolled_course, payment, due])
        print("Entry successful!!!!!!!!!!!!")


if num==3:
    with open('student_list.csv','r') as f:
        data = pd.read_csv(f)
        print(tabulate(data,headers='keys',tablefmt='psql'))


if num==4:
    csv_file = 'student_list.csv'
    with open('txt_file.txt', "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
        my_output_file.close()
    def editContact():
        obj2 = open("txt_file.txt", "r")
        val=str(input("What do you want to update: "))
        old = raw_input("Enter old "+val+ ": " )
        new = raw_input("Enter new " + val + ": ")

        s = re.sub(old, new, obj2.read())

        obj1 = open("txt_file.txt", "w")
        obj1.writelines(s)
        print("Successful")
    editContact()

    df = pd.read_csv('txt_file.txt',delimiter='|')
    print(df)
    df.to_csv('student_list.csv',index=False)


if num==5:
    lines = list()
    members = input("Please enter a member's name to be deleted.")
    with open('student_list.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field.split('|')[0] == members:
                    lines.remove(row)
                    print("successful")
                else:
                    break
    with open('student_list.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)




