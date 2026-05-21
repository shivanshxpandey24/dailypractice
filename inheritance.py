# INHERITANCE
'''
1. Single Inheritance
2. Multiple Inheritance
3. Multi-level Inheritance
4. Hierarchichal Inheritance
5. Hybrid Inheritance
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

