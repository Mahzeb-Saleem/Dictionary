# Student Registration System
# Students have to choose from four courses: AIC, CNC, BCC, IoT
# Following are the course codes:
# AIC = a
# CNC = b
# BCC = c
# IoT = d

all_students=[]
for i in range(1,3):
    Name=input('Enter Student Name: ')
    Cell_no=input('Enter Cell no: ')
    Cnic_no=input('Enter CNIC no: ')
    Email=input('Enter email adress: ')
    Age=input('Enter Age: ')
    Courses=['AIC', 'CNC', 'BCC', 'IoT']
    a=Courses[0]
    b=Courses[1]
    c=Courses[2]
    d=Courses[3]
    Course=[]
    Course=input('Enter Course code: ')
    print('-'*20)
    Bio_data={
                'Name': Name,
                'Cell no': Cell_no,
                'Cnic no': Cnic_no,
                'Email': Email,
                'Age': Age,
                'Courses': Course
            }
    all_students.append(Bio_data)
print(all_students)
