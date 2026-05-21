# class SharmaVishnu:
#     a = 'lolo'     # CLASS KE ANDAR KE VARIABLES ARE CALLED ATTRIBUTES
    
#     def sample():  # CLASS KE ANDAR KE FUNCTION ARE CALLED METHODS
#         print('This is a Sample Function')
    
# SharmaVishnu.sample()
# print(SharmaVishnu.a)

# class Animals:
#     name = "Animal"
    
#     def greet(self):     
#         # JAb bhi class ke ANDAR KE FUNCTION KO OBJECT KI HELP SE CALL KARENGE TO USSEY EK PARAMETERE DENA HOGA
#         print('This is Animal Class')
        
# tau = Animals()  # Here Tau is Object --> Class Stored in variable is called Object
# mama = Animals()
# mama.greet()


# # CREATE A TASK WHICH WILL PERFORM TWO TASKS 
# # 1. Greet the user - "This is______class "
# # 2. Addind up two no.

# class Add:
#     def greet(self):
#         print(" hello from shivansh")
        
#     def add(self):
#         a=10
#         b=20
#         print(a+b)
        
# obj = Add()
# obj.greet()
# obj.add()
        
        
# CLASS METHOD --> this can help on changing the class attributes 

class Animal():
    name = "Dog"
    
    # Instance(Object) can never change your class attributes
    @classmethod
    def change(cls,new):
        cls.name=new
        print(cls.name)
        
mehu = Animal()
mehu.change('Cat')
print(Animal.name)     
        
        
# STATIC METHOD --> function can be runned without help of object and given parameters....
# it is independent of object matlab obj bane ya na bane ghanta farak nhi padta
class bjp:
    @staticmethod
    def neta():
        print('Modih Ji')
        print('Raghav Chaddha')
        print('Amit Shah')
        
new_market = bjp()
new_market.neta()
   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  
      