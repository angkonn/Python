import numpy as np
# Creating a 2d array
a_2d=np.array([[1,2,3,4],[5,6,7,8]])
print(a_2d)
type(a_2d)

a=np.zeros(4)
a

# identity maxtrix:
a=np.identity(4)
a

a=np.arange(10)
a
b=np.arange(15,30)
b

# to print numbers in certain distance, suppose 3:
c=np.arange(5,50,3)
c

# to print odd numbers from 1 to 30:
a=np.arange(1,31,2)

# to print even numbers from 1 to 30:
b=np.arange(2,31,2)
a,b

# Properties of Numpy:
#     1. Shape
#     2. Dimension
#     3. Size
#     4. Data Type

# Shape:
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
a.shape


# to see dimension:
a.ndim

# to see size:
a.size


 # to see datatype:
a.dtype

# to convert integer to float:
b=a.astype('float')
b

# Indexing and Iteration:
# Reshape:
a=np.arange(30).reshape(2,15)
# 2 means there will be 2 division and 15 means there will be
# 15 elements in each division
print(a)

# Slicing Operation:
a=np.arange(20)
print(a)
print(a[:5])
print(a[2:10])
print(a[3:])

a=np.array([[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,10,11,12],[14,15,16,17,18,19,20,21,22]])
print(a)
# Suppose we need to print values of 2nd row to the 5th value
# So, for 2nd row, the index is 1, and for 5th value , the index is 5
print(a[1][:5])
# also,
print(a[0][:5])
print(a[1][1:])

# Also, suppose we need to print the 5th column:
print(a[:,4])

# If we want to print something using loop:
for i in a:
    print(i)
# at first, i takes the value of first row, then 2nd and then 3rd 

# to print in one line using loop:
for i in a:
    for j in i:
        print(j,end=' ')

# OPERATIONS:
a=np.array([12,23,354])
b=np.array([2,3,4])

# Addition:
print(a+b)
# Division:
print(a/b)
#multiplication:
print(a*b)

# if we want to check if the elements of an array 
# is greater or less than a number:
a>2000

# To find max. value of the elements of an array:
print(a.max())
# To find min. value of the elements of an array:
print(a.min())
# To find mean value of the elements of an array:
print(a.mean())
print(a.std())

# Reshaping:
a=np.array([[1,2,3,4,5,6,7,8,9],[4,5,6,7,8,9,10,11,12],[14,15,16,17,18,19,20,21,22]])
a

# 2d to 1d array:
a.ravel()


# To convert to a transpose matrix: 
a.transpose()


# Functions of Numpy:
# Random Value Generator:
#random value from 0 to 1
np.random.random()

np.random.seed(1)
np.random.random()

# suppose we want random values from 1 to 30:
np.random.uniform(1,30)

# suppose we want random values from 1 to 30 in an array of 5 elements:
np.random.uniform(1,30,5)

# Only Integer:
np.random.randint(1,100)

# to return the index of maximum value: 
a=np.array([1,2,5,3,6,3,2])
print(a)
print(np.argmax(a))

# to return the index of minimum value: 
print(np.argmin(a))

# to sort the array:
print(np.sort(a))

# to sort the array in decreasing order:
print(np.sort(a)[::-1])


