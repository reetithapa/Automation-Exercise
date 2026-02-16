a={1,3,9,6,9}
print(a)        #shows unordered
#print(a[2])     #unindexed
print(type(a))
print(len(a))

#add values
a={1,3,9,6,9}
a.add(7)
a.add(12)        #adding element in mulltiple lines
print(a)

#adding value in single line
a={1,3,9,6,9}
a.update([7,12])
print(a)

#remove
a={1,3,9,6,9}
a.remove(1)
print(a)

#removing the value from set without knowing where it is available in the set or not
a={1,3,9,6,9}
a.discard(15)
print(a)

#randomly remove the value from the set
a={1,3,9,6,9}
a.pop()
print(a)
a.pop()
print(a)

#removing all the values at a go from the set
a={1,3,9,6,9}
a.clear()
print(a)

#deleting the set
a={1,3,9,6,9}
#del a
#print(a)

#using for loop
a={1,3,9,6,9}
for e in a:
    print(e)

#use in and not in operator
a={1,3,9,6,9}
print(3 in a)
print(3 not in a)
print(15 in a)
print(15 not in a)

#Set can nest only tuple. set cannot nest list and set
a={1,(2,5,9,11),3,9,6,9}
print(a)

#converting list to a set
a=[1,3,9,6,9]
b=set(a)
print(type(a))
print(type(b))

#union
a={1,3,9,6,9}
b={4,8,5,2,3}
print(a.union(b))    #print(a|b)
print(a.intersection(b))     #print(a&b)
print(a.difference(b))       #print(a-b) or print(b-a)
print(a.symmetric_difference(b))    #print(a^b)

#min max sum
a={1,3,9,6,9}
print(max(a))
print(min(a))
print(sum(a))










