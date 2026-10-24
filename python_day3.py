# 1.("string")
# 2.("slicing concept=[start:stop:step]")
# 3.("string_built_in_function_in python")
# ["len()"]="returns the length of the string"
# ["title()"]="returns the first letter of string in upperCase and rest in lowerCase"
# ["lower()"]='returns all the string characters in lowercase'
# ["upper()"]="returns all the string characters in uppercase"
str="hello,bro!! hello,hello"
print(str.count("hello",12,25))#count(substring,start,end)count how much time this substring comes in string
print(str.count("hello"))
print(str.find("hello",10,20))#returns the first index value of substring in string
print(str.endswith("llo"))
print(str.startswith("hell"))
print(str.isalnum())
print(str.isspace())
print(str.islower())
print(str.istitle())
print(str.split())
print(str.split("bro"))#don't include that word
print(str.partition("bro"))#substring before,seprator,substring after
str1="Hello World"
print(str1.islower())
print(str1.isupper())
print(str1.istitle())
print(str1.replace("H","O"))
str2="    PriyanshiSharma  "
print(str2.lstrip())
print(str2.rstrip())
print(str2.strip())
print("-".join(str2))
