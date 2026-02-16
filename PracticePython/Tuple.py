a=(1,4,7,9,3,6)
print(a)
print(type(a))

#accessing tuple
a=(1,4,7,9,3,6)
print(a[0])
print(a[1])        #all these are forward index
print(a[2])
print(a[3])

print(a[-2])  #backward index

#we cannot use append(), insert(), remove() and pop() commands
#sort() and reverse are not possible()
#when a= (1,2,3,4,5)
#a[0]=9 is not possible

#length of tuple same as listt
a=(1,4,7,9,3,6)
print(len(a))

#using for loop in tuple
a=(1,4,7,9,3,6)
for i in range(len(a)):
    print(a[i])

for e in a:
    print(e)

#slicing
a=(1,4,7,9,3,6)
print(a[1:4])
print(a[:4])
print(a[:])

#using in and not in operator same as list
a=(1,4,7,9,3,6)
print(7 in a)
print(15 in a)
print(15 not in a)

#count() sum() min() max() index() del a type() all are same as list

#nested tuple
a=(1,4,(1,5,2,8,6),7,9,3,6)
print(a[2])
print(a[2][2])
#a[2][2]=9   #not possible  tuple inside tuple is not possible

#nested tuple with list    only list inside tuple is mutable
a=(1,4,[1,5,2,8,6],7,9,3,6)
print(a[2])
print(a[2][2])
a[2][2]=9
print(a)

#typecasting a string to a tuple
a=tuple("Reeti")
print(type(a))

for e in a:
    print(e)


















