List="this store multiple datatype and is mutable,square bracket[],ordered sequence,it can store tuple,even another list"
list=[45,5.5,'shivansh']
print(list)
list1=[["shivansh",12,7],7035,("priyanshi",28,"b.tech")]
list2=['my dearest-']
print(list1)
print(list[0])
#print(list[5])#error
print(list1[-1])
print(list+list1)#list concatenation
print(list2*5)#repitation
print("shivansh" in list1)#False->#membership
print("shivansh" not in list1)#True
print("shivansh" in list1[0])#True
print(list1[0:2])#slicing
print(list1[0:])
print(list1[:2])
print(list[:])
print(list[::-1])#reverse the whole list
print(list[1::-1])
print(list[0:-1])
#----------------------------------------------------------------------------------
"List built-in-function"
list3=[13,45,67,89]
print(len(list3))
link=list()
str1='aeiou'
link=list(str1)
print(link)
list3.append(90)#pass the value
print(list3)
list4=[20,30]
list3.extend(list4)
print(list3)
list3.insert(4,88)#pass the value with index
print(list3)
print(list3.count(89))#pass the value
print(list3.index(67))#pass the value to get the index of that particular value
print(len(list3))
list3.remove(13)#pass the value
print(list3)
print(len(list3))
print(list3.pop(4))#pass the index list3=[45,67,89,20,30]
print(list3.pop())#if no index is given directly delete the last index
list3.reverse()
print(list3)
list3.sort()#list3.sort(reverse=true)->sort in descending order
print(list3)
list6=sorted(list3)
print(list6)#leave the previous list as it is and make a new sort list and store it in another list and also take the extra space
print(min(list4))
print(max(list4))
print(sum(list4))

import sys
list=[]
i=1
while i<=200:
    list.append(i)
    i+=1
print(list)

z=sys.getsizeof(list)
print(z)