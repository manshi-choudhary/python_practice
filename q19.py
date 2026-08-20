class calculator:
    def __init__(self,x):
        self.x=x
    def square(self):
        return self.x**2
    def cube(self):
        return self.x**3
    def square_root(self):
        return self.x**0.5
x= int(input("enter the number :"))
num= calculator(x)
print(f"Cube of {x} is {num.cube()}\nSquare of {x} is {num.square()}\nSquare root of {x} is {num.square_root()}")