#--------------ENCAPSULATION------------------------------------------------

class Animals:
    name = "Lion"  # Public Attribute
    _age=12   # Protected Attribute
    __height=120 #Private Attribute
    
    def speak(self):   # Public Object Method
        print('The Lion Roars')
        
    def _Walks(self):  # Protected Object Method
        print("The Lion Is Walking")
        
    def __Sleeps(self):  # Private Object Method
        print("The LIon Is Sleeping")
        
        
obj1= Animals()
# print(obj1.__height)
# obj1.__sleep()

#-----PRIVATE ATTRIBUTES AND METHODS CAN NOT BE ACCESSED BY YOUR OBJECTS AND INHERITED CLASSES-----    
        
        
        
        