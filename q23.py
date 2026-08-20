class twoDvector:
    def __init__(self,i,j):
        self.i= i
        self.j= j
    def show(self):
        print(f"the two dimensional vector is: {self.i}i + {self.j}j")

class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k= k
    def show(self):
        print(f"the three dimensional vector is: {self.i}i + {self.j}j + {self.k}k")

a= twoDvector(2,3)
a.show()
b= threeDvector(2,3,4)
b.show()