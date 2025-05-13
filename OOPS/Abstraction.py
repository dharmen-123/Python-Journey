### Abstraction 
# Abstrtact class-> used  atleast one Abstrtact method decorator
# Abstrtact method-> used  Abstrtact method decorator with no body
# Concrete method -> method name with body 


from abc import ABC,abstractmethod

# class A(ABC):
#     def first(self):
#         print("from first method")
        
        
#     @abstractmethod
#     def second(self):
#         pass
#     @abstractmethod
#     def third(self):
#         pass

###########################################

class Senior(ABC):
    def add(self ,x,y):
        return x+y
    def sub(self ,x,y):
        return x-y
    @abstractmethod
    def div(self ):
         pass
class Junior(Senior):
    def mul(self ,x,y):
        return x*y
    def div(self ,x,y):
        return x/y
obj=Junior()
a=obj.div(10,20)
print(a)