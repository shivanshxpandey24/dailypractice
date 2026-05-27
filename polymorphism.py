#-----------------POLYMORPHISM--------------------------

class Animals:
    def speak(self):
        print("Animals are Shouting")
        
class Humans:
    def speak(self):
        print('Humans Are Speaking')
        
obj1=Animals()
obj2=Humans()

obj1.speak()
obj2.speak()

# BOTH THE SPEAK METHODS ARE APPEARS TO BE SAME BUT BOTH HAVE DIFFERENT TASK AND THIS IS KNOWN AS 
# POLYMORPHISM

"""  METHOD OVERRIDING """

class Reebok:
    def __init__(self,material,size):
        self.material=material
        self.size=size
        
    def details(self):
        print(self.material)
        print(self.size)
        
class Campus(Reebok):
    def __init__(self,material,size,colour):
        super().__init__(material,size)
        self.colour=colour
        
    def details(self):
        print(super().details())
        print(self.colour)
        
obj1= Campus("lether",10,"grey")

obj1.details()

# a child class object has the power to call methods and attributes  of a parent class but it
# cannot call the details method of its patrent class cause that details method is OverRidden and
# this concept is known as Method OverRiding


"""   METHOD OVERLOADING   """

class Animal:
    def hello(self,a):
        print('How Are you ?')
        
    def hello(self,a,b):
        print("kaise ho ?")
        
# Method Overloading is a concept where you define similar name methods inside a single class with
# different parameters