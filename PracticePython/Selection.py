#if statement
a=2
b=4

if a>b:
    print("a is greater than b")

print("End of program")

#if else statement
a=5
b=4

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

print("End of program")

#if elif else statement
a=10
b=15
c=20
d=5
e=1
if a<b:
    print("a is less than b")
elif b<c:
    print("b is less than c")
elif c<d:
    print("c is less than d")
elif d<e:
    print("d is less than e")
else:
    print("e is the least")