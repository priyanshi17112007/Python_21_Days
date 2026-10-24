"""-----------------------Introduction to Pandas-----------------------
Pandas store tabular data using a Dataframe.
A Dataframe is 2-D labelled Data-structure like a table in Datatbase.
Every Dataframe contain rows and column and has both the row and column index.
Each column have different types of values.
"""
import pandas as pd
students = [
    (1, "Priya", 85, "Submitted", 90),
    (2, "Rahul", 42, "Pending", 65),
    (3, "Aman", 20, "Pending", 30),
    (4, "Sneha", 95, "Submitted", 98),
    (5, "Rohit", 60, "Submitted", 75)
]
df=pd.DataFrame(students,columns=["ID","NAME","ATTENDENCE","ASSIGNMENT","MARKS"])
print(df)

dt = pd.read_csv("college_student_tracker.csv")#by name
dt = pd.read_csv("D:/college_student_tracker.csv")#by location/path
print(dt)

"""-------------Operations in Pandas-------------------------"""
print(df.head(2))#return top 5 rows or data
print(df.tail(2))#return bottom/last rows or data
print(df.shape)#return how many rows/column
print(df.size)
print(df.columns)
print(df.NAME)#select single columns
print(df[["NAME","ATTENDENCE"]])#select multiple columns
print(df.dtypes)
print(df.values)
print(df.index)
print(df.loc[2])#give the data of that particular row
print(df.loc[[1,3,4]])#select multiple rows
print(df.iloc[3])#select single row by integer index
print(df.iloc[[1,3,4]])#select multople rows by integer index
print(df[df["ATTENDENCE"]>60])#FILTERING ROWS
df["PHONE_NO"]=[342445,3434556,67657,1233455,436456]#add a new column or if give same values then df["phone_no"]=10
print(df)
df.insert(3,"present",["yes","no","yes","yes","no"])#ADD A COLUMN AT PARTICULAR INDEX
print(df)
print(df.drop(columns=["PHONE_NO"]))#DELETE A COLUMN
print(df.rename(columns={"NAME":"STU_NAME"}))#RENAME OR GIVE NEW NAME TO A COLUMN
del df["present"]#delete a column from dataframe
print(df)
print(df.drop(2))#delete a particular row
df.loc[2] = [3, "Aman", 42, "Pending", 65,786876876]#give value at that particular row
print(df)
df.loc[2,"ATTENDENCE"]=92
print(df)