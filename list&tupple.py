#ListAndTypple:

fruits=['apple','banana','orange'] #this is a list

# List can be modified

fruits.append('mango')
print(fruits)

fruits.remove('apple')
print(fruits)


folmul=fruits.copy()
print(folmul)


num=[10,20,30,40,50]
print(num[1])
 

print(num[0::2])

#2D list


matrix=[1,2,3],[1,2,3],[1,2,3]
print(matrix)
print(matrix[0][0])


# tuples: Cannot be modified: Immutable
num=[0,1,2,3,4,5]
numb=(0,1,2,3,4,5)
print(type(num))
print(type(numb))
