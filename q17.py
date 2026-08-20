#oops
class employee:
    name= ""
    age= 0
    city= ""
    def __init__(self, name, age, city): #constructor
        self.name = name
        self.age = age
        self.city = city
    @staticmethod
    def greet():
        print("good evening!!")
    def info(self):
        print(f"hey there the name is {self.name} age is {self.age} and city is {self.city}")

a= employee("miku",18,"nnl")
print(a.name,a.age,a.city)
a.greet()
a.info()