"""-----------------Sorting in Numpy Array--------------------------
1.np.sort()
2.np.argsort()
3.ndarray.sort()
"""
#Sorting in 1-D Array
import numpy as np
x=np.array([8,2,1,45,23,12])
y=np.sort(x)
z=np.sort(x)[::-1]
print(x)
print(y)
print(z)

w=np.argsort(x)#return the index of sorted array
print(w)

x.sort()
print(x)

#Sorting in 2-D Array
import numpy as np
arr1=np.array([[12,11,15],
              [23,32,42],
              [67,76,87]])
y=np.sort(arr1)#by default do row-wise axis=1
z=np.sort(arr1,axis=0)#sort column-wise
print(y)
print(z)

m=np.argsort(arr1)
n=np.argsort(arr1,axis=0)#sort column-wise
print(m)
print(n)

arr1.sort()#in place sort
print(arr1)

"""Statistical Operations in Numpy:1-D Array"""
import numpy as np
array1=np.array([89,4,67,1090,7,2,56])
arr=np.max(array1)#max()
rr=np.min(array1) #min()
a=np.sum(array1) #sum()
mean=np.mean(array1) #mean()
me=np.median(array1) #median()-first sort in ascending then find hte middle element
print(mean)
print(a)
print(rr)
print(arr)
print(me)
print(np.prod(array1))#prod()


array2=np.array([8,3,7,2,1])
print(np.var(array2))#VARIANCE
print(np.std(array2))#standard variance