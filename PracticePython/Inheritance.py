class A:
    a=9
    def method_a(self):
        print("Inside method_a")

class B(A):
    b=10
    def method_b(self):
        print("Inside method_b")

obj = B()
print(obj.a)
print(obj.b)
obj.method_a()
obj.method_b()

# single inheritance
class A:
    a=9

class B(A):
    b=10

obj = B()
print(obj.a)
print(obj.b)

#multilevel
class A:
    a=9

class B(A):
    b=10

class C(B):
    c=11

obj = C()
print(obj.a)
print(obj.b)
print(obj.c)

#hierarchical
class A:
    a=9

class B(A):
    b=10

class C(A):
    c=11

#multiple
class A:
    a=9

class B:
    b=10

class C(A,B):
    c=11

#hybrid
class A:
    a=9

class B(A):
    b=10

class C(A):
    c=11

class D(B,C):
    d=12

obj = D()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)







