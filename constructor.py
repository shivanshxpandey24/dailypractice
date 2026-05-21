#CONSTRUCTOR  --> it is represented by __init__ ( Dunder Methods)
# Constructor is the function jo sabse pehle execute hote hai.....
# ......doesn't matter ki inke neeche ya upar koi function hai ki nahi 
class SharmaVishnu:
    def greet(self):
        print("This is greet Function")
        
    def __init__(self,name,age):
        self.name = name   #Instance Attribute
        self.age = age
        print("This is Constructor Function.")
        print(self.name)
        print(self.age)
        
    def menu(self):
        print("Paneer Kulche")
        
obj = SharmaVishnu("Shivansh", 18)
obj.menu()
    
       
# Q.make a class which will take 3 two no. as input create 
# 1. two instance attribute
# 2. crete a function which will print greatest among them
 
class Sample:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def greater (self):
        if self.a > self.b:
            print(self.a , ' is bada')
        else:
            print(self.b,' is bada')
            
obj=Sample(10,20)
obj.greater()
        
    