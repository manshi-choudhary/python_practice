class employee:
    company= "microsoft"
    def __init__(self, name, salary, role):
        self.name= name
        self.salary= salary
        self.role= role

n= int(input("enter the number of employees :"))
for i in range(n):
    name= input("enter the name of employee :")
    salary= int(input("enter the salary of employee :"))
    role= input("enter the role of employee :")
    a= employee(name,salary,role)
    print(f"the name is {a.name}\n salary is {a.salary}\n and role is {a.role}\n and company is {a.company}")

