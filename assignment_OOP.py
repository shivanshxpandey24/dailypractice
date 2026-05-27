class Student:
    def __init__(self,name,age,email,phone):
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone
        
    def Details(self):
        print('Name of Student :- ', self.name)
        print(' Age of Student :- ' , self.age)
        print(' Email of Student :- ',self.email)
        print(' Phone no. of the Student :- ' ,self.phone)
        
class Class10thAdmission(Student):
    def __init__(self,name,age,email,phone):
        super().__init__(name,age,email,phone)
        print("!!!ADMISSION SUCCESSFULL!!!")
        
class Class12thAdmission(Student):
    def __init__(self,name,age,email,phone):
        super().__init__(name,age,email,phone)
        
        if int(self.age) >= 16:
         print("!!!ADMISSION SUCCESSFULL!!!")
        else:
            print("!!!ADMISSSION FAILED!!!")
        
            
print("Press 1 for Admission in 10th class")
print("Press 2 for Admission in 12th class")

choice = int(input("Enter your choice:- "))

name=input("Tell your Name :- ")
age=input("Tell your Age :- ")
email=input("Tell your Email :- ")
phone=input("Tell your Phone No. :- ")

if choice==1:
    student1 = Class10thAdmission(name,age,email,phone)
    student1.Details()
        
if choice==2:
    student1 = Class12thAdmission(name,age,email,phone)
    student1.Details()
        

    