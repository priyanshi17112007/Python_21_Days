"---------------------Map & Filter in python-----------------"
#==========map===============================
marks = [77, 97, 64, 85, 55]
def grade(marks):
    if marks >= 90:
        return 'A'
    elif 80 <= marks < 90:
        return 'B'
    elif 70 <= marks < 80:
        return 'C'
    elif 60 <= marks < 70:
        return 'D'
    else:
        return 'F'
    
grades=list(map(grade,marks))#map
print("marks are:",marks)
print("grades are:",grades)


def square(number):
    return number * number
numbers = [2, 3, 4, 5]
result = map(square, numbers)
print(next(result))#itertive-individual
print(list(result))

#=================filter========================
number=[44,99,89,79,69,22]
def filtering(score):
    return score<60

result=filter(filtering,number)
print("failing scores",list(result))

"------------------lambda functions--------------------"
list1=[1,34,55,77,89,90,88]
result=list(filter(lambda x:x%2==0,list1))
print(result)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x * x, even_numbers)
print(list(squares))