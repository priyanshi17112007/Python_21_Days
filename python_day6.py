"""In python there are four forms of cONDITIONAL Statements:-
1.if Statement
2.if-else Statement
3.if...elif...else Statement
4.nested if Statement
"""
age=int(input("enter ur age:"))
if age>=18:
    print("u are eligible to give vote")
print("Ur Vote ur Voice")

age1=int(input("enter ur age:"))
if age1>=18:
    print("u are eligible to give vote")
else:
    print("u are under 18")
    
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Topper! Even Google asks you questions!!")
elif marks >= 60:
    print("Good job! Parents are happy today")
elif marks >= 33:
    print("Pass! Bhagwan ne bacha liya")
else:
    print("Fail! Time to change your identity")
    
age3 = int(input("enter ur age:"))
own_car="false"
if age3>=18:
    if own_car=="true":
        print("u can drive a car")
    else:
        print("buy ur own car")
else:
    print("Pehle bade to ho jao")
