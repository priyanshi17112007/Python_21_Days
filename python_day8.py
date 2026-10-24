#    Error in Python:-Syntax Error,Runtime Error,Logical Error
list1=[12,45,67]
print(list1[4])#Runtime Error-IndexError

a=5
b=10
average=a+b/2 # Logical Error
print(average)

c=9
print(b)#Name Error-Runtime Error

x='20'
y=10
print(x/y)#Type Error-Runtime Error

str1="hello,Dear"
str1.reverse()#Attribute Error-no function present in string

x=0
while x<20:#logical Error-infinite loop
    print(x)
    
x=int("hello")
print(x)#Value Error

list2=[0]*1000000000
print(list2)#memory error