class animal:
    def __init__(self,species):
        self.species= species
    def show(self):
        print(f"the spieces is {self.species}")
class dog(animal):
    def __init__(self,species,name):
        super().__init__(species)
        self.name=name
    def show(self):    
        print(f"the name of the dog is {self.name}")
class bark():
    @staticmethod
    def sound():
        print("bow bow!")

a= animal("dog")
a.show()
b= dog("dog","rocky")
b.show()
c= bark()
c.sound()