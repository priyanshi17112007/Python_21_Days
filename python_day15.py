"""------------------Genrators in python---------------"""
def creator():
    i=1
    while i<=200:
        yield i
        i+=1
print(creator)
x=creator()
print(next(x))
print(next(x))
print(list(x))

"---------------------List Comprehension in Python------------"
marks=[34,67,89,90,99]
new_marks=[x+2 for x in marks]
print(new_marks)

#print the cube of 1 to 10 only even numbers
cube=[]
for x in range(1,11):
    if x%2==0:
        cube.append(x**3)
print("cubes of even no. from 1 to 10",cube)
# by List Comprehension,print the cube of 1 to 10 only even numbers
cubes=[x**3 for x in range(1,11) if x%2==0]
print(cubes)

#-------------------------------------------------------
list=[12,56,90]
print(list.append(100))#add only one element
print(list.extend([100,2200,500]))#add multiple elements in list
print(list)

#---------------------------------------------------------
set1={12,34,45}
set1.add(35)#add only one element in immutable
set1.update({88,100})
print(set1)

#[expression for item in iterable if condition]
list2=[i*i for i in range(1,14) if i%2==0]
print(list2)