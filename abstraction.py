"""   ABSTRACTION  """
# abstraction is like a set of rules which you give to your subclasses....it is enforced to subclasses
# to follow those rules

# from abc import ABC , abstractmethod

# class Shapes(ABC):
#     @abstractmethod
#     def area():
#         pass
    
#     @abstractmethod
#     def perimeter():
#         pass
    
# class Square(Shapes):
#     def __init__(self,side):
#         self.side=side
        
#     def area(self):
#         print(self.side * self.side)
        
#     def perimeter(self):
#         print(4*self.side)
        
# class Circle(Shapes):
#     def __init__(self,radius):
#         self.radius=radius
        
#     def area(self):
#         pass
    
#     def perimeter(self):
#         pass
    
# obj = Square(10)


"""  DUNDER METHOD  """

# class Robots:
#     a=12
#     def __init__(self,name):
#         self.name=name
        
#     def __str__(self):
#         return f"hello my name is {self.name}"
    
# obj1 = Robots("Alpha")
# obj2 = Robots("Beta")

# print(obj1)
# print(obj2)


class Number:
    def __init__(self,value):
        self.value=value
        
    def __add__(self,other):
        return self.value + other.value
    
    def __eq__(self,value):
        return self.value == value.value
    
a = Number(20)
b = Number(30)
 