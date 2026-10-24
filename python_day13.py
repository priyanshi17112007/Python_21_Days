"""-------------------Functions in Python--------------------------
def function_name(parameter):
statement that defines what the function does
return value
"""
def college_life(name):
    print("Hello", name)
    print("Attend classes!!!")
    print("Complete assignments!?")
    print("Drink chai <<<>>>>")
    print("Survive exams ::::")

college_life("Priyanshi")

"""---------------------File Handling--------------------"""
f1=open("doc.txt")
print(f1.read())#read
f1.close()
f=open("doc.txt","w")#write
f.write("u are future AI Engineer")
f.close()
f2=open("doc.txt","a")#append
f2.write("\n So practice it daily")
f2.close()
f3 = open("doc.txt", "r")#read the append content
print(f3.read())#f3.read(7)read only starting 7 character
print(f3.tell())#pointer on which index
print(f3.seek(2))#move the pointer at their specific position
print(f3.tell())

f3.seek(0)
for line in f3:
    print(line)

f3.seek(0)
print(f3.readline())#read only first line
f3.close()

f3 = open("doc.txt")
print(f3.readlines())#read the lines and give in list format

