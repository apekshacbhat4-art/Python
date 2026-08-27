import os
import time
class StudentDatabase :
      def __init__(self,roll_no,name,age,sub,marks):
          self.Marks={}
          tot=0
          self.roll_no=roll_no
          self.name=name
          self.age=age
          for i in range(len(sub)) :
              self.Marks[sub[i]]=marks[i]
              tot+=marks[i]
          self.total=tot
          self.per=self.total/len(marks)
          if 90<=self.per<=100 :
              self.grade="A+"
          elif 80<=self.per<=89 :
              self.grade="A"
          elif 70<=self.per<=79 :
              self.grade="B"
          elif 60<=self.per<=69 :
              self.grade="C"
          elif 50<=self.per<=59 :
              self.grade="D"
          else:
              self.grade="Fail"
          self.rank=None



STUDENT=[]
students=[]
sub=[]
print("\t\t\t\t*** STUDENT DATABASE SYSTEM ***")
n=int(input("Enter number of students: "))
n_sub=int(input("Enter number of subjects: "))
for i in range (n_sub) :
    sub.append(input(f"Enter subject {i+1} name: "))
time.sleep(1)
os.system("cls")
for i in range (n) :
    marks=[]
    print(f"\t\t\t*** STUDENT {i+1} ***")
    roll_no=int(input("Enter roll no: "))
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    for j in range (n_sub) :
        marks.append(float(input(f"Enter marks for {sub[j]} (out of 100): ")))
    STUDENT.append(StudentDatabase(roll_no,name,age,sub,marks))
    print()
    print(f"Total marks: {STUDENT[i].total}")
    print(f"Percentage: {round(STUDENT[i].per,2)}%")
    print(f"Grade: {STUDENT[i].grade}")
    print(f"Student {name} added succesfully!")
    time.sleep(3)
    os.system("cls")
def class_top():
    max1=0
    max1_name=''
    max1_grade=""
    max_rol=0
    for i in range(n):
        if STUDENT[i].per>max1:
            max1=STUDENT[i].per
            max1_name=STUDENT[i].name
            max1_grade=STUDENT[i].grade
            max_rol=STUDENT[i].roll_no
    return max1_name,max_rol,max1,max1_grade

def class_report():
    print("\n******************************************")
    print("        STUDENT DATABASE REPORT")
    print("******************************************")
    print("Roll No  Name       Age  Percentage  Grade")
    print("------------------------------------------")
    tot=0
    for i in range(n) :
        print(f"{STUDENT[i].roll_no:<9}{STUDENT[i].name:<11}{STUDENT[i].age:<5}{STUDENT[i].per:<12}{STUDENT[i].grade:<5}")
        tot+=STUDENT[i].per
    print("------------------------------------------")
    print(f"Total students : {n}")
    print(f"Class Average : {round(tot/n,2)}%")
def student_report(ID):
    print("****************************************")
    print("      STUDENT REPORT CARD")
    print("****************************************")
    print(f"Roll No    : {STUDENT[ID].roll_no}")
    print(f"Name       : {STUDENT[ID].name}")
    print(f"Age        : {STUDENT[ID].age}")
    print("----------------------------------------")
    print("Subject        Marks")
    print("----------------------------------------")
    for subject, mark in STUDENT[ID].Marks.items():
        print(f"{subject:<15}{mark}")
    print("----------------------------------------")
    print(f"Total Marks  : {STUDENT[ID].total}")
    print(f"Percentage   : {STUDENT[ID].per}%")
    print(f"Grade        : {STUDENT[ID].grade}")
    print("****************************************")
def sub_top():
    print("*** SUBJECT TOPPERS ***")
    for i in range(n_sub) :
        maxi_name,max_marks="",0
        for j in range(n) :
            if STUDENT[j].Marks[sub[i]]>max_marks:
                maxi_name,max_marks=STUDENT[j].name,STUDENT[j].Marks[sub[i]]
        print(f"{STUDENT[i].Marks:<9} : {maxi_name}  ({max_marks}) ")
def fail_list():
    fail=False
    print("Roll No  Name     Percentage  Grade")
    for i in range(n):
        if STUDENT[i].per<50:
            print(f"{STUDENT[i].roll_no}        {STUDENT[i].name}    {STUDENT[i].per}%    Fail")
            fail=True
    if fail==False:
        print("No students have failed!!")
def add_std():
    marks = []
    roll_no=int(input("Enter roll no: "))
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    for j in range (n_sub) :
        marks.append(float(input(f"Enter marks for {sub[j]} (out of 100): ")))
    STUDENT.append(StudentDatabase(roll_no,name,age,sub,marks))
    print("Student added successfully!!")
def delete_std():
    r=int(input("Enter roll no to delete: "))
    for i in range(n):
        if r==STUDENT[i].roll_no:
            NAME=STUDENT[i].name
            del STUDENT[i]
            print(f"Student {NAME} deleted successfully!!")
            return

print("****************************************\n        STUDENT DATABASE SYSTEM\n****************************************\n1. Class Report")
print("2. Student Report\n3. Class Topper\n4. Subject Topper\n5. Failures List\n6. Add Student\n7. Delete Student\n8. Exit\n****************************************")
choice=1
while choice in range(1,9):
    choice=int(input("\nEnter your choice:"))
    if choice not in range(1,9):
        print("Invalid choice!")
        choice=1
    elif choice==1:
        class_report()
    elif choice==2:
        flag=False
        print("Search by:\n1. Name\n2. Roll No")
        search_choice=int(input("Enter choice: "))
        if search_choice==1:
            s=input("Enter name of student :")
            flag=True
        else:
            R=int(input("Enter roll no of student : "))
        for i in range(n):
            if flag is True :
                if s==STUDENT[i].name:
                    ID=i
                    student_report(ID)
                    break
            else:
                if R==STUDENT[i].roll_no:
                    student_report(i)
                    break
    elif choice==3:
        top_name,top_rol,top_per,top_grade=class_top()
        print("*** CLASS TOPPER ***")
        print(f"Name       : {top_name}")
        print(f"Roll No    : {top_rol}")
        print(f"Percentage : {top_per}")
        print(f"Grade      : {top_grade}")
    elif choice==4:
        sub_top()
    elif choice==5:
        fail_list()
    elif choice==6:
        add_std()
    elif choice==7:
        delete_std()
    else:
        break
