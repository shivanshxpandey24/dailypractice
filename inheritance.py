# INHERITANCE
'''
1. Single Inheritance --> 1 Parent and 1 Child Class
2. Multiple Inheritance --> 2 Parent and 1 Child class
3. Multi-level Inheritance --> One child class becomes parent of another class
4. Hierarchichal Inheritance --> 1 Parent class and multiple Child Class
5. Hybrid Inheritance --> Combination of two types of Inheritance
'''

# 1. SINGLE INHERITANCE
class Parent:
    def __init__(self):
        print("this is a parent class constructor")
    
    def greet(self):
        print('this is a parent class')
        
class Child(Parent):
    def __init__(self):
        print("this is a child class constructor")
    def show(self):
        print('this is a child class')
        
obj = Child()
obj.greet()
obj.show()




class Factory:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
        
    def show(self):
        print(f"{self.name}'s Bag of {self.colour} colour" )
        
class Wildcraft(Factory):
    def __init__(self,name,colour,zip,pocket):
        super().__init__(name,colour)
        self.zip=zip
        self.pocket=pocket
        
    def display(self):
        print(f"{self.name}'s Bag of {self.colour} colour , has {self.zip} zips and {self.pocket} Pockets")

obj = Wildcraft("Shivansh","Grey", 4 , 9)
obj.display()
    
# 2. MULTIPLE INHERITANCE -->  2 Parent and 1 Child class

class Father: #Parent1

    def _init_(self):
        print('This is Father class constructor')

    def greet_father(self):
        print('This is Father class')

class Mother: #Parent2
    def _init_(self):
        print('This is Mother class constructor')

    def greet_mother(self):
        print('This is Mother class')


class Child(Mother,Father): #Child
    #If we have to run constructor of Father class first
    
    def _init_(self):
        Father._init_(self) #Sabse pehle Father class ka constructor will be run
        Mother._init_(self) #After Father class Mother class constructor will be run

obj = Child()
obj.greet_father()
obj.greet_mother()




# MULTILEVEL INHERITANCE  --> One child class becomes parent of another class

class A: # Super Parent Class
    def greet(self):
        print('This is Class A')

class B(A):  # Parent Class
    def show(self):
        print("This Is Class B")
        
class C(B):  # Child Class
    def detail(self):
        print("This is Class C")
        
obj=C()
obj.show()
obj.detail()
obj.greet()
    
    
    
class CEO:  # Super Parent Class
    def __init__(self):
        print("This is a CEO class constructor")
        
class Manager(CEO):   # Parent Class
    def __init__(self):
        super().__init__()
        print("This is a Manager class constructor")
        
class Employee(Manager):  # Child Class
    def __init__(self):
        super().__init__()
        print("This is Employee Class Constructor")
    
kill = Employee()



# HIERARCHIAL INHERITANCE --> 1 Parent class and multiple Child Class

class Parent:
    def greet(self):
        print("This is Parent Class")
        
class Child1(Parent):
    pass

class Child2(Parent):
    pass

obj = Child2()
obj.greet()

obj2 = Child1()
obj2.greet()




class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def Details(self):
        print(f"Hello {self.name} you have {self.balance}")
        
class Saving(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        print(f" This is a Saving Class Constructor {self.name} , {self.balance} ")
        
class Current(Account):
    def __init__(self,name,balance,type):
        super().__init__(name,balance)
        self.type = type
        print(f" This is a Current Class Constructor {self.name} , {self.balance} , {self.type}")
        
obj = Current("shivansh" , 800 , "Saving For Her")