Dictionary="is a data structure similar to hash table,unordered collection,key&value,mutable"
#its key must be unique and this are immutable like strings,number and tuples
dict={11:"ashish",12:"aman",13:"akshay",14:"jalak"}
print(dict.get(12))
# search sequesntially so the time complexity is goes upto o(n)
dict1={}
for i in range(6):
    if i%2==0:
        dict1[i]=i*i
print(dict1)  

#by dictionary comprehension
list3={i:i*i for i in range(1,14) if i%2==0}
print(list3) 