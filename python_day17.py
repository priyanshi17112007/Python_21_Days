"""==================Decorator in python=================
Decorator is a function that takes another function as argument and returns a function"""
def decorator(func):
 def wrapper(*args,**kwargs):
  print("transaction is initiated")
  func(*args,**kwargs)
  print("Transaction is completed")
 return wrapper
 
@decorator
def add(a,b):
 print("sum:",a+b)
 
add(1,2)


