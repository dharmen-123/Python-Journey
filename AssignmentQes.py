class Factorial:
    def __init__(self,fact):
        self.fact=fact
    def facto(self,n):
        for i in range(n,1):
           fact=fact*i
        print(fact)
obj=Factorial(1)
obj.facto(5)
