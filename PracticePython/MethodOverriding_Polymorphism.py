class A:
    a=5
    def sample(self):
        print("Inside sample method of class A")

class B(A):
    a=10
    def sample(self):
        print("Inside sample method of class B")

obj = B()
print(obj.a)
obj.sample()
