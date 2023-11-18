import json
import os

def LoadStudent(FilePath):
    try:
        with open(FilePath,'r') as file:
            Database=json.load(file)
    except FileNotFoundError:
        Database=[]
    return Database

def SaveStudentData(Database,FilePath):
    with open(FilePath,'w') as file:
        json.dump(Database,file,indent=2)

def AddData(Database,NewStudent,FilePath):
    Database.append(NewStudent)
    print("\nStudent '"+NewStudent['FullName']+"' added successfully.")
    DisplayData(NewStudent)
    SaveStudentData(Database,FilePath)

def DeleteStudent(Database,StudentName,FilePath):
    for i in Database:
        if i['FullName'].lower()==StudentName.lower():
            Database.remove(i)
            print("\nStudent '"+StudentName+"' record deleted.")
            SaveStudentData(Database,FilePath)
            return
    print("\nStudent '"+StudentName+"' not found.")

def ShowStudentsList(Database):
    for i in Database:
        DisplayData(i)

def DisplayData(Student):
    print("\nStudent Information:\n")
    for Key,Value in Student.items():
        print(Key,":",Value)
    print()

def SearchList(Database,StudentName):
    for i in Database:
        if i['FullName'].lower()==StudentName.lower():
            DisplayData(i)
            return
    print("\nStudent '"+StudentName+"' not found.")

def SetCriteria(Database,criteria):
    FilteredStudent=[i for i in Database if criteria(i)]
    for i in FilteredStudent:
        DisplayData(i)

def UpdatingStudentData(Database,StudentName,Updation,FilePath):
    for i in Database:
        if i["FullName"].lower()==StudentName.lower():
            i.update(Updation)
            print("\nStudent '"+StudentName+"' record updated.")
            DisplayData(i)
            SaveStudentData(Database,FilePath)
            return
    print("\nStudent '"+StudentName+"' not found.")

def PercentageGrade(Marks):
    Percent=sum(Marks.values())/len(Marks)
    if Percent>=90:
        return Percent,'A+'
    elif 80<=Percent<90:
        return Percent,'A'
    elif 70<=Percent<80:
        return Percent,'B'
    elif 60<=Percent<70:
        return Percent,'C'
    elif 50<=Percent<60:
        return Percent,'D'
    else:
        return Percent,'F'

FilePath=os.path.abspath('StudentRecords.json')
Database=LoadStudent(FilePath)

while True:
        print("\n\t\t\tStudent Management Application\n")
        print("1. Show Students List")
        print("2. Filter Students Data")
        print("3. Search for a Student")
        print("4. Update Student's Record")
        print("5. Remove a Student")
        print("6. Add Student")
        print("7. Get Average Percentage of a Class (Bonus)")
        print("8. Calculate Average Marks of a Student (Bonus)")
        print("9. Exit Console")

        n=int(input("\nEnter your n (1-9): "))
        if n in range(1,10):
            if n==1:
                print("\nFetching...")
                ShowStudentsList(Database)
            elif n==2:
                CriteriaFor=input("\nEnter criteria (e.g., Class=10A)\n\nCriteria's for filtering were listed :\n1. FullName\n2. Age\n3. DateOfBirth\n4. Class\n\nCriteria : ")
                CriteriaItems=[tuple(item.split('=')) for item in CriteriaFor.split(',')]
                Criteria=lambda student: all(item in student.items() for item in CriteriaItems)
                FilteredStudents=[i for i in Database if Criteria(i)]
                print("\nFiltering...")
                for student in FilteredStudents:
                        DisplayData(student)
            elif n==3:
                StudentName=input("\nEnter student's Full Name: ")
                print("\nSearching...")
                SearchList(Database,StudentName)
            elif n==4:
                StudentName=input("\nEnter student's Full Name: ")
                UpdationFor=input("\nEnter updated information in the format 'key1=value1,key2=value2' : \n\nArea's for Updation :\n1. FullName\n2. Age\n3. DateOfBirth\n4. Class\n5. SubjectsList ( Value For this should be list of Subjects )\n6. Marks ( Format should be Dict - Subjects as Key and Mark as Value )\n\nKindly Enter Data were Updation Required : ")
                Updation=dict(item.split('=') for item in UpdationFor.split(','))
                print("\nUpdating...")
                UpdatingStudentData(Database,StudentName,Updation,FilePath)
            elif n==5:
                StudentName=input("\nEnter student's Full Name: ")
                DeleteStudent(Database,StudentName,FilePath)
            elif n==6:
                NewData={
                    'FullName':input("\nEnter Full Name: "),
                    'Age':input("Enter Age: "),
                    'DateOfBirth':input("Enter Date of Birth: "),
                    'Class':input("Enter Class: "),
                    'SubjectsList':input("Enter Subjects List (comma-separated): ").split(','),
                    'Marks':{subject:int(input("\nEnter Marks for "+subject+" : ")) for subject in input("Enter Subjects Name for which Marks are available to Enter  \n( Enter Subjects by comma-separated ) : ").split(',')}
                }
                print("\nInserting...")
                AddData(Database,NewData,FilePath)
            elif n==7:
                ClassName=input("\nEnter the class name: ")
                print("\nCalculating...")
                SetCriteria(Database,lambda x: x.get('Class')==ClassName)
                Percent=[PercentageGrade(student['Marks'])[0] for student in Database]
                AveragePercentage=sum(Percent)/len(Percent)
                AverageRounded=round(AveragePercentage,2)
                print("\nAverage Percentage of Class "+ClassName+" :",AverageRounded)
            elif n==8:
                StudentName=input("\nEnter student's FullName: ")
                print("\nCalculating...")
                for i in Database:
                    if i['FullName'].lower()==StudentName.lower():
                        Marks=i['Marks']
                        AverageMark=sum(Marks.values())/len(Marks)
                        AverageRounded=round(AverageMark,2)
                        print("\nAverage Marks of "+StudentName+" :",AverageRounded)
                        break
                else:
                    print(f"\nStudent '{StudentName}' not found.")
            elif n==9:
                print("\nEntering Sleep Mode...")
                print("\t\t\tExiting, Thank you! ")
                break
        else:
            print("\nInvalid Choice. Please enter number between 1 and 9")
        print("\nIf you want to continue...\n\tPress 1 \nelse: \n\tPress 2")
        m=int(input("\nYour Choice Please : "))
        if m==2:
            print("\nEntering Sleep Mode...")
            print("\t\t\tExiting, Thank you! ")
            break
        else:
            print("\nHere we go again !")