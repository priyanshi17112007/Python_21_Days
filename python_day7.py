#     Loops in Python
""" For loop is applied over sequence(string,tuple,list)
eg:-for i in colours:,
for i in range(1,10):
"""
""" While loop is repeatedly execute as long as  certain condition is True"""
x=0
while not(1<=x<=100):
   x=int(input("enter a no. between 1 to 100:"))
print("valid no:",x)    

for i in range(4):
    x=int(input("enter a no. between 1 to 100:"))
    if 1<=x<=100:
        print("valid no:",x)
        break
    else:
        print("Invalid no.Try Again")
        
# do while condition in form of while in Python
i=0
while True:
    print(i)
    i+=1
    if i>0:
        break
    
# keywords for loops:-break,continue,pass
list1=range(4)
for i in list1:
    if i==2 :
        break
    print(i)
    
list2=range(4)
for i in list2:
    if i==2 :
        continue
    print(i)
    
name=input()
for i in name:
    if (i==" "):
        break
    print(i,end='')
    
message = input("Did you get a reply? (yes/no): ")
if message == "yes":
    print("That's wonderful! ")
elif message == "no":
    pass
print("Stay positive and keep smiling!!!")
