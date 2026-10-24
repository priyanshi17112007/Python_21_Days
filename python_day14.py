"""-------------Intrduction of OOPS in Python-------------
1.Object are real world entities.
2.Classes are group of these entities.
3.Classes are blueprint or templates of an object.

"""

class employee:
    def putdata(self):
        self.id = int(input("Enter employee ID: "))
        self.name = input("Enter employee name: ")
        self.salary = float(input("Enter employee salary: "))

    def display(self):
        print("Employee ID:", self.id)
        print("Employee name:", self.name)
        print("Employee salary:", self.salary)


a = employee()
a.putdata()
a.display()

class student:
    def __init__(self,id,name,marks):#dunder
        self.id=id
        self.name=name
        self.marks=marks
        
    def average(self):
        return sum(self.marks)/len(self.marks)
    
e=student(101,"naman",[10,20,30,40])
print(e.name)
print(e.average())


"------Inheritance in python--------"

class Employee:
    def __init__(self):
        print("I am an Employee")

    def show(self):
        print("Employee name: Priyanshi")


class Developer(Employee):
    def __init__(self):
        super().__init__()
        print("I am a Developer")

    def show(self):
        super().show()
        print("Skill: Python Programming")


d = Developer()
d.show()
