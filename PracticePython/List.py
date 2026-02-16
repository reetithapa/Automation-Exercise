a=[9,1,7,5]
print(a)

#access the elements of lists
#we nedd to understand indexing
a=[9,1,7,5]
print(a[2])
print(a[3])

#size of list we nedd to use len function
a=[9,1,7,5]
print(len(a))

#use for loop with range
for i in range(len(a)):
    print(i)    #it prints index i.e 0,1,2,3

for i in range(len(a)):
    print(a[i])    #prints the content of a variable

#for each loop
a=[1,2,5,77,23,9]
for num in a:
    print(num)

#updating elements in list
a=[1,2,4,7,8]
print(a)
a[2]=10
print(a)

#appending the elements at the end of the list
a=[1,2,4,7,8]
print(a)
a.append(9)
print(a)

#inserting elements a certain index position
a=[1,2,4,7,8]
print(a)
a.insert(1,10)
print(a)

#removing element from list
a=[1,2,4,7,8]
print(a)
a.remove(1)
print(a)

#using pop to remove last element
a=[1,2,4,7,8]
print(a)
a.pop()
print(a)

#using pop to remove particular element of idex
a=[1,2,4,7,8]
print(a)
a.pop(1)
print(a)

#prints the removed element
print(a.pop(1))

#removing all
a=[1,2,4,7,8]
print(a)
a.clear()
print(a)

#reverse
a=[1,2,4,7,8]
print(a)
a.reverse()
print(a)

#sort
a=[1,2,4,7,8]
print(a)
a.sort()
print(a)


a=[1,2,4,7,8]
colors=["orange","green","blue","red"]
print(colors)
colors.sort()
print(colors)

#using index
a=[1,2,4,7,8]
print(a)
print(a.index(8))

#nested list
a=[1,[6,3,9,2],4,7,8]
print(a[1][3])

#different type of values in same list
a=["Honda","Amaze",14.5,"Petrol",True,90000]
print(a[3])

#forward index and backward index
a=[1,2,4,7,8]
print(a[2])    #forward
print(a[-2])    #backward  -2+5 th index

#slicing
a=[1,2,4,7,8]
print(a[:])    #0 index to last element or position
print(a[1:3])    #index 1 to position 3 i.e 2,4
print(a[:4])     #index 0 to 4th element

#find no. of times element is repeated in the list
a=[1,2,4,7,8,1,5,1,3,1,1,1,1]
print(a.count(1))

#finding max and min value in lsit
a=[1,2,4,7,8]
print(max(a))
print(min(a))

#sum of elemetns in list
a=[1,2,4,7,8]
print(sum(a))

#find data type of list
a=[1,2,4,7,8]
print(type(a))

#deleting the list
a=[1,2,4,7,8]
print(a)
#del a
#print(a)

#using in and not in operator with list
a=[1,2,4,7,8]
print(5 in a)   #false
print(7 in a)    #true

#concatenating two list using + operator
a=[1,2,4,7,8]
b=[2,7,4,9,1]
c=a+b
print(c)

#extend existing list
a=[1,2,4,7,8]
b=[2,7,4,9,1]
a.extend(b)
print(a)
print(b)














